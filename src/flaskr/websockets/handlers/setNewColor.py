from flaskr.websockets.sock import sock, CurrentSocketConnection
import json


@sock.route("/setNewColor")
def setNewColorHandler(ws):
    global CurrentSocketConnection
    while True:
        data = ws.receive()
        print(data)
        data_json = json.loads(data)
        Connections = list(filter(lambda conn: str(conn["device_id"]) == str(data_json["device_id"]),
                                  CurrentSocketConnection[data_json["device_type_id"]]))
        print(Connections)
        print(CurrentSocketConnection)
        if Connections.__len__() != 0:
            Connections[0]["connection"].send(data)
