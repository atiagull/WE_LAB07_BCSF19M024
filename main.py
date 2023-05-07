from flask import Flask,render_template,request,redirect,url_for
from base import engine, base,session
from task import task

base.metadata.create_all(engine)
session =session()

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        tk = request.form["task"]
        t = task(title, tk)
        session.add(t)
        session.commit()
        return render_template("home.html")
    else:
        return render_template("home.html")

@app.route("/add")
def add():
    return "<h1>added</h1>"
@app.route("/show_records")
def show_records():
    val = session.query(task).all()
    return render_template("show_table.html",records=val)
if __name__=="__main__":
    app.run(debug=True)