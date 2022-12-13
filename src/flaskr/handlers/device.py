from flaskr.app import app
from flaskr.handlers.index import devices
from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta


records = [[], []]


@app.route("/device", methods=["POST", "GET"])
def device():

    id = int(request.args["id"])
    device_item = devices[id]

    time = datetime(year=2022, month=1, day=1, hour=0, minute=0)

    timeInfo = []

    for i in range(0, 24 * 2):
        timeInfo.append({
            "time": time.strftime("%H:%M"),
            "status": "avalible"
        })
        time += timedelta(minutes=30)

    if request.method == "POST":
        records[id].append(dict(request.form))

    for r in records[id]:
        startIndex = datetime.strptime(r["startTime"], "%H:%M")
        startIndex = (startIndex.hour * 60 + startIndex.minute) // 30
        endIndex = datetime.strptime(r["endTime"], "%H:%M")
        endIndex = (endIndex.hour * 60 + endIndex.minute) // 30

        print(startIndex, endIndex)

        for i in range(startIndex, endIndex):
            timeInfo[i]["status"] = "unavalible"

    print(timeInfo)

    return render_template("device.html",  timeInfo=timeInfo, device=device_item)
