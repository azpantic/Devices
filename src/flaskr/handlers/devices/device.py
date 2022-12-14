from flaskr.app import app
from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta
from flaskr.data_base.FDataBase import dBase


@app.route("/device", methods=["POST", "GET"])
def device():

    id = int(request.args["id"])
    device = dBase.getDeviceById(id)

    time = datetime(year=2022, month=1, day=1, hour=0, minute=0)

    timeInfo = []
    for i in range(0, 24 * 2):
        timeInfo.append({
            "time": time.strftime("%H:%M"),
            "status": "avalible"
        })
        time += timedelta(minutes=30)

    operations = dBase.getItemOperationsHistory(id)


    for r in operations:
        startIndex = r.startTime
        startIndex = (startIndex.hour * 60 + startIndex.minute) // 30
        endIndex = r.endTime
        endIndex = (endIndex.hour * 60 + endIndex.minute) // 30

        #print(startIndex, endIndex)

        for i in range(startIndex, endIndex):
            timeInfo[i]["status"] = "unavalible"

    print(timeInfo)

    return render_template("devices/device.html",  timeInfo=timeInfo, device=device)
