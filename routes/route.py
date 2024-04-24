from server import app
from database.db import *
from flask import render_template, request

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

@app.route("/register_user", methods=["post"])
def register_user():
    name, lastname, id, birthday = request.form["name"], request.form["lastname"], request.form["id"], request.form["birthday"]
    insert_record()
    return render_template("home.html")