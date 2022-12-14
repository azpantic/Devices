from flaskr.app import app
from flask import render_template , request, flash
from flask_login import login_required

from flaskr.data_base.models import Device
from flaskr.data_base.FDataBase import dBase
from flaskr.loginmanager.loginmanager import administrator_required

@app.route("/addDevice", methods = ["POST" , "GET"])
@login_required
@administrator_required
def addDevice():
    
    if request.method == "POST":
        
        form = request.form
        title  = form["Title"]
        uid = form["uid"]
        description = form["Description"]
        newDevice : Device = Device(title= title , uid = uid, description=description )
        
        if dBase.getDeviceByUID(uid) != None:
            flash("Id должен быть уникальным")
        else:
            dBase.addDevice(newDevice)
        
    return render_template("devices/addDevice.html")