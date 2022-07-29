# VISUALIZATION OF CONDENSED MULTIPLE SEQUENCE ALIGNEMENTS AND PHYLOGENETIC TREES


### List of participants and affiliations:
- Christian Zmasek (czmasek@jcvi.org) - Team leader
- Chrissy Aceves (caceves@scripps.edu)
- Nate Matteson (natem@scripps.edu)
- Grace Nabakooza (sxv8@cdc.gov)
- Daniel Chen (dchen32@uw.edu)
- Diana Ir (diana.ir@state.co.us)

## Table of content
   1. Introduction
   2. Project goal
   3. Prerequisites
   4. Installation
   5. Input
   6. Approach
   7. Future work
   
   
  
## Introduction
Phylogenetic visualization of large multiple sequence alignments is difficult. Since phylogenies are reconstructed based on differences in a multiple sequence alignment (MSA), tools that utilize only the positions with variation in the MSA could improve phylogenetic reconstruction and visualization.

## Project goal
We developed a drag and drop interface where the user provides (1) a vcf file and (2) a newick tree file and we render a multiple sequence alignment (MSA) visualization focusing on single nucleotide variants (SNVs).

## Prerequisites
Python 3
- dendropy
- flask
-JavaScript
-Web-Interface


# How to use our tool

## Installation
The app can be simply run by executing `python app.py` in the user's command line interface (e.g. Terminal, Command Prompt).

## Input
Example VCF and Newick (also called New-Hampshire) file formats are provided in the  `example-data` folder. Upload the files at "http://127.0.0.1:5000/" then click "Visualize Data" and it will render.

## Approach
- Create two HTML pages one to submit files and the other to render them
- Create a Flask app to connect Python parsing and webpage output
- Utilize JS to create Drag and Drop system
- Alter React-MSA's underlying code to only show variants of interest

## Future Work
- Summarize nucleotides at reference positions
- Annotate phylogeny with other metadata
- Highlight items on the tree itself
- Real-time calculation of clade-defining substitutions
- Increased options and flexibility in design/algorithms utilized
- More fleshed out website and user interface
