from flaskr.websockets.sock import sock, CurrentSocketConnection
import json


@sock.route("/sock/device")
def getNewColorHandler(ws):
    global CurrentSocketConnection
    Device_Data = json.loads(ws.receive())

    CurrentSocketConnection[Device_Data["device_uid"]] = ws

    while True:
        pass
