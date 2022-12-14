from flaskr.app import app
from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta
from flaskr.data_base.FDataBase import dBase
from flaskr.data_base.models import Operation , Device
from flask_login import login_required, current_user
from datetime import datetime
from flaskr.websockets.sock import CurrentSocketConnection

@app.route("/newOperation" , methods= ["POST"])
def newOperation():
    
    id = int(request.args["id"])
    form = request.form

    bookingDate = form["bookingDate"][2::]
    #bookingDate = bookingDate.replace("-" , "/")
    startTime = form["startTime"]
    endTime = form["endTime"]

    newOperation : Operation = Operation(userId = int(current_user.get_id()),
        deviceId = id, startTime = datetime.strptime(f"{bookingDate} {startTime}" , "%y-%m-%d %H:%M"),
        endTime = datetime.strptime(f"{bookingDate} {endTime}" , "%y-%m-%d %H:%M")
        )
    
    dBase.addNewOperation(newOperation)



    return redirect(url_for("device", id=id))