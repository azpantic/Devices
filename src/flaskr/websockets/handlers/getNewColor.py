from flaskr.websockets.sock import sock, CurrentSocketConnection
import json


@sock.route("/getNewColor")
def getNewColorHandler(ws):
    global CurrentSocketConnection
    Device_Data = json.loads(ws.receive())
    print(Device_Data)
    if Device_Data['device_type_id'] not in CurrentSocketConnection:
        CurrentSocketConnection[Device_Data['device_type_id']] = []

    CurrentSocketConnection[Device_Data['device_type_id']].append({
        "device_name": Device_Data['device_name'],
        "connection": ws,
        "device_id":  Device_Data['device_id']
    })
    print(CurrentSocketConnection)
    while True:
        pass
