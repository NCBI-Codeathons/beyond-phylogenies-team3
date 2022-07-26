from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():   
   render_template("./src/display.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
