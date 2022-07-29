import os
import sys
from flask import Flask, render_template, request, redirect, url_for

sys.path.insert(1,  "./scripts")
import parse_vcf
import parse_newick

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='./tmp'

try:
    os.mkdir(app.config['UPLOAD_FOLDER'])
except:
    print("Cannot Create", app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET'])
def home():
    #allows the user to upload a vcf and newick file
    return(render_template("dropzone.html"))

@app.route('/visualize-tree', methods=['GET', 'POST'])
def visualize_tree():
    if request.method == "POST":
        files = request.files['file']
        if files.filename.endswith(".vcf"):
            files.save(os.path.join(app.config['UPLOAD_FOLDER'],"temp.vcf"))
        elif files.filename.endswith(".nwk"):
            files.save(os.path.join(app.config['UPLOAD_FOLDER'],"temp.nwk"))
        return redirect(url_for('visualize_tree'))

    elif request.method == "GET":
        f_vcf = os.path.join(app.config['UPLOAD_FOLDER'], "temp.vcf")
        f_tree = os.path.join(app.config['UPLOAD_FOLDER'], "temp.nwk")

        #load tree and output tree as string
        tree = parse_newick.parse_newick(tree_loc=f_tree)
        #load vcf and output psuedo-alignment
        vcf = parse_vcf.parse_vcf( vcf_loc=f_vcf )
        #render the html to webpage
        return(render_template("display.html", tree=tree, msa=vcf))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
