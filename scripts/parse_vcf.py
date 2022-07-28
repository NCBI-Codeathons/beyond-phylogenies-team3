"""
Parses a vcf file for multiple sequences into a variant object,
then returns a list of raw strings with each representing the
collapsed sequence alignment for a single file.
"""
import os
import sys
import argparse
import numpy as np
from typing import List, Tuple

class Variant():
    def __init__(self):
        self.pos = 0
        self.allele_map = {}
        self.sequence = []

    def set_allele_map(self, allele_ref: str, allele_alt: str):
        """
        Maps alleles to numeric values.
        """
        alt_list = allele_alt.split(",")
        base_count = 1
        self.allele_map = {"0":allele_ref, ".": allele_ref}
        for alt in alt_list:
            self.allele_map[str(base_count)] = alt
            base_count += 1

    def assign_info(self, info_list: List):
        """
        Expands the one-hot encoding to actual sequence.
        """
        self.sequence = [self.allele_map[x] for x in info_list]

def to_fasta( entries: List[Tuple[str, str]], ref: str ) -> str:
    """
    Converts list of names and sequences to a fasta string
    """
    return_str = [
        "# STOCKHOLM 1.0",
        "#=GF ID   EXAMPLE"
    ]
    for entry in entries:
        return_str.append( f"{entry[0]}\t{entry[1].decode()}" )

    return_str.append( f"#=GC seq_cons\t{ref}")
    return_str.append( "//" )
    return_str = "\n".join( return_str )
    return return_str

def parse_vcf( vcf_loc: str ) -> List[str]:
    variant_collection = []
    ref = []
    with open( vcf_loc, 'r') as vfile:
        for count,line in enumerate(vfile):
            line = line.strip()
            #first line needs to be the file format
            if count == 0:
                file_format = line.split("=")[-1]
                if file_format != "VCFv4.2":
                    raise("File format incorrect, accepts v4.2")
                    sys.exit(1)

            #defines the vcf file format specs
            if line.startswith("##"):
                continue
            #this line is the header
            if line.startswith("#"):
                header_list = line.split("\t")[9:]
                total_sequences = len( header_list )
                print("Total files in .vcf:", total_sequences )
                continue

            #3 is ref 4 is alt
            line_list = line.split("\t")
            new_variant = Variant()
            ref.append( line_list[3] )
            new_variant.set_allele_map("-", line_list[4])
            new_variant.assign_info(line_list[9:])

            variant_collection.append(new_variant)

    #define a matrix (x,y) where x is the variants and y is the sequences
    char_array = np.chararray((len(variant_collection), total_sequences))
    for count, vc in enumerate(variant_collection):
        char_array[count,:] = vc.sequence
    transposed_array = char_array.T
    list_array = [row.tostring() for row in transposed_array]

    if len(list_array) != total_sequences:
        raise("Error in sequence conversion")

    return( to_fasta( zip( header_list, list_array ), "".join( ref ) ) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse a vcf file to object')
    parser.add_argument( '--vcf', help='vcf file to parse' )
    args = parser.parse_args()
    result = parse_vcf( vcf_loc=args.vcf )
    print( result )
