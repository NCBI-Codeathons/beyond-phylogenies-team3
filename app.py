import sys
from flask import Flask, render_template

sys.path.insert(1,  "./scripts")
import parse_vcf
import parse_newick

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    #allows the user to upload a vcf and newick file
    return(render_template("dropzone.html"))

@app.route('/visualize-tree', methods=['GET'])
def visualize_tree():
    #load tree and output tree as string
    # TODO: Point tree_loc at file from dropzone.html
    tree = parse_newick.parse_newick( tree_loc="example-data/bp_masked_alignment.nwk" )
    #load vcf and output psuedo-alignment
    # TODO: point vcf_loc at file from dropzone.html
    vcf = parse_vcf.parse_vcf( vcf_loc="example-data/bp_masked_alignment.vcf" )
    #render the html to webpage
    return( render_template("display.html", tree=tree, msa=vcf ) )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
