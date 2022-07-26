import sys
from flask import Flask, render_template

sys.path.insert(1,  "./scripts")
import parse_vcf

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home(): 
    #load tree
    #output tree as string
    #load vcf and output psuedo alignment
    #render the html to webpage
    return(render_template("display.html"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
