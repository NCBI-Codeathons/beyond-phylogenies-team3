"""
Parses a vcf file for multiple sequences into a variant object,
then returns a list of raw strings with each representing the 
collapsed sequence alignment for a single file.
"""
import os
import sys
import argparse
import numpy as np
parser = argparse.ArgumentParser(description='Parse a vcf file to object')
parser.add_argument('--vcf',
                    help='vcf file to parse')
args = parser.parse_args()

class Variant():
    def __init__(self):
        self.pos = 0
        self.allele_map = {}
        self.sequence = []

    def set_allele_map(self, allele_ref, allele_alt):
        """
        Maps alleles to numeric values.
        """
        alt_list = allele_alt.split(",")
        base_count = 1
        self.allele_map = {"0":allele_ref, ".": allele_ref}        
        for alt in alt_list:
            self.allele_map[str(base_count)] = alt
            base_count += 1

    def assign_info(self, info_list):
        """
        Expands the one-hot encoding to actual sequence.
        """
        self.sequence = [self.allele_map[x] for x in info_list]

variant_collection = []
with open(args.vcf, 'r') as vfile:
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
            line_list = line.split("\t")
            total_files = len(line_list[9:])
            print("Total files in .vcf:", total_files)
            continue
 
        #3 is ref 4 is alt
        line_list = line.split("\t")
        new_variant = Variant()
        new_variant.set_allele_map(line_list[3], line_list[4])
        new_variant.assign_info(line_list[9:])
        
        variant_collection.append(new_variant)

#define a matrix (x,y) where x is the variants and y is the files
char_array = np.chararray((len(variant_collection), total_files))
for count, vc in enumerate(variant_collection):
    char_array[count,:] = vc.sequence
transposed_array = char_array.T
list_array = [row.tostring() for row in transposed_array]

if len(list_array) != total_files:
    raise("Error in sequence conversion")

return(list_array)
