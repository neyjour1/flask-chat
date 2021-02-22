from flask import request, session
from flask_socketio import SocketIO
import constants

flask_clients = {}
clients = {}

class Server:
    def __init__(self, app):
        self.messages = []
        self.io = SocketIO(app)
        self.io.on_event('connect', self.connect)
        self.io.on_event('chatmessage', self.handle_message)
        self.io.on_event('disconnect', self.disconnect)
        self.io.on_event('clear', self.clear)

    def handle_message(self, data):
        # client = clients[request.sid]
        # if(not client): return
        print(data)
        if(not self.is_valid_message(data["message"])): return
        user = session.get(constants.SESSION)
        self.messages.append({"name": user, "message": data["message"], "UTCdate": data["UTCdate"]})
        self.io.emit("chatmessage", self.messages[len(self.messages)-1])
        # print(formatted)

    def clear(self, data):
        print("borrando...")
        self.messages.clear();
        self.io.emit("firstmessage", self.messages)


    def disconnect(self):
        clients.pop(request.sid, None)

    def connect(self):
        if(session.get(constants.SESSION)):
            user = session[constants.SESSION]
            # if(request.sid): clients.append(client)
            # clients[request.sid] = {"id": request.sid, "name": flask_clients[request.sid].name}
            # print("Nuevo usuario: " + request.sid + "!")
            print("user: " + user)
            # print(clients)
            self.io.emit("firstmessage", self.messages)
            return
        print("not logged")
        return


    def is_valid_message(self, message):
        if not message.strip():
            return False
        return True
