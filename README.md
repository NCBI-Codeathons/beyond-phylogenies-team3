TITLE 


Introduction

#The problem
Phylogenetic visualization of large and closely related sequences is difficult. Since phylogenies are reconstructed based on differences in a multiple sequence alignment (MSA), tools that utilize only the positions with variation in the MSA could improve phylogenetic reconstruction and visualization. Single nucelotide variants (SNVs) are easily extracted from MSA and stored in Variant Call Format (VCF). 


#Workflow Description
Our workflow creates a drag and drop interface where the user provides (1) a vcf file and (2) a tree file and render a visualization focusing on SNVs.

Written by 


Resources

VCF format resources
https://github.com/moonso/vcf_parser
https://github.com/GMOD/vcf-js
https://www.ebi.ac.uk/training/online/courses/human-genetic-variation-introduction/variant-identification-and-analysis/understanding-vcf-format/
https://samtools.github.io/hts-specs/VCFv4.2.pdf
Parsing with Pandas: https://www.biostars.org/p/416324/
Usher: https://usher-wiki.readthedocs.io/en/latest/UShER.html, Uses protobuf format which stores a mutation annotated tree object

JavaScript resources
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction

D3 resources
https://observablehq.com/@d3/gallery


Considerations/Issues
1. Labels for MSA positions
2. NA vs AA


Prerequisites/ Dependencies
Python 3

Input

Output


Installation



References


