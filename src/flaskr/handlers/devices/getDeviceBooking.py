from flaskr.app import app
from flask import request
from datetime import datetime
from flaskr.data_base.FDataBase import dBase


@app.route("/getDeviceBooking")
def getDeviceBooking():

    device_id = int(request.args["device_id"])
    date = request.args["booking_date"]

    print(device_id, date)

    return dBase.getDeviceOperationOnDate(device_id, datetime.today())
