import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Parse a vcf file to object')
parser.add_argument('--vcf',
                    help='vcf file to parse')
args = parser.parse_args()

class Variant():
    def __init__(self):
        self.chrom = ''
        self.pos = 0
        self.ref = ''
        self.alt = []
        self.info = []
        self.filename = ''

    def assign_info(self, info_list):
        pass

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
            continue
 
        line_list = line.split("\t")
        new_variant = Variant()
        #TODO:ADD LINE TO VCF OBJ

        #APPEND VCF OBJ TO LIST
        
