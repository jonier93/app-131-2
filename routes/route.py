from server import app
from flask import render_template

@app.route("/")
def view_home(): 
    return render_template("home.html")  

@app.route("/home")
def view_home2():
    return render_template("home.html")

@app.route("/register")
def view_register():
    return render_template("register.html")

@app.route("/consult")
def view_consult():
    return render_template("consult.html")