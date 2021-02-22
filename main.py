from flask import Flask, request
from ioserver import Server
from datetime import timedelta
import constants

app = Flask(__name__)

if __name__ == "__main__":
    app.config["SECRET_KEY"] = constants.SECRET_KEY
    app.permanent_session_lifetime = timedelta(days=constants.SESSION_LIFETIME_DAYS)
    from views import chat
    from auth import auth
    app.register_blueprint(chat)
    app.register_blueprint(auth)
    server = Server(app)
    app.run(host=constants.HOST, port=constants.PORT, debug=True)
