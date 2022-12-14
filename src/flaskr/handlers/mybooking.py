from flaskr.app import app
from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta
from flaskr.data_base.FDataBase import dBase
from flask_login import current_user

@app.route("/myBooking" , methods = ["POST" , "GET"])
def myBooking():
    

    if request.method == "POST":
        args = request.args

        if args["operationType"] == "cancel":
            dBase.deleteOperationById(int(args["operationId"]))

        

    userId = int(current_user.get_id())

    operations = dBase.getUserOperations(userId)

    for op in operations:
        op.device_title = dBase.getDeviceById(op.deviceId).title

        if op.startTime <= datetime.now() and op.endTime >= datetime.now():
            op.status = "active"
        
        if op.startTime <= datetime.now() and op.endTime <= datetime.now():
            op.status = "completed"
        
        if op.startTime >= datetime.now() and op.endTime >= datetime.now():
            op.status = "waiting"


    return render_template("user/mybooking.html" , operations=operations)