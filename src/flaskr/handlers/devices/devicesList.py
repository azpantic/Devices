from flaskr.app import app
from flaskr.data_base.FDataBase import dBase
from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta

@app.route("/devicesList")
def devicesList():

    devices = dBase.getAllDevices()
    print(devices)

    return render_template("devices/devicelist.html" , devices=devices)