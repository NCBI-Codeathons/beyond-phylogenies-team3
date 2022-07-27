import sys
from flask import Flask, render_template

sys.path.insert(1,  "./scripts")
import parse_vcf

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    #allows the user to upload a vcf and newick file
    return(render_template("dropzone.html"))

@app.route('/visualize-tree', methods=['GET'])
def visualize_tree():
    #load tree
    #output tree as string
    #load vcf and output psuedo alignment
    #render the html to webpage
    return(render_template("display.html"))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
