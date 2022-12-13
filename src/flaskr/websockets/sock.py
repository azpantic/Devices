from flask_sock import Sock
from flaskr.app import app

sock = Sock(app)


CurrentSocketConnection = {}
