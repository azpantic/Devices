from flaskr.app import app
from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta


@app.route("/")
def init():
    return redirect(url_for("index"))


devices = [

    {
        "title": "Розетка",
        "id": "0"
    },

    {
        "title": "Паяльник",
        "id": "1"
    },

]


@app.route("/index")
def index():

    return render_template("index.html", devices=devices)
