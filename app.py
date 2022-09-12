from flask import Flask,request,render_template 
from time import ctime
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return ctime


if __name__=="__main__":
    app.run(debug=False)
