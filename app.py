import sys
from flask import Flask, render_template

sys.path.insert(1,  "./scripts")
#import parse_vcf
import parse_newick

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home(): 
    #load tree as string
    tree = parse_newick.parse_newick( tree_loc="example-data/bp_masked_alignment.nwk" )
    #load vcf and output psuedo alignment
    #render the html to webpage
    return(render_template("display.html", tree=tree))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
