from flask import Blueprint, render_template, request, redirect, url_for, session
from ioserver import flask_clients
from auth import auth
import constants

chat = Blueprint('chat', __name__, template_folder='templates')

@chat.before_request
def check_login():
    if(not session.get(constants.SESSION)):
        # no logueado
        return redirect("login")
    if(not session.get(constants.SESSION) in flask_clients):
        flask_clients[session.get(constants.SESSION)] = {"name": session.get(constants.SESSION)}


@chat.route('/logout')
def logout():
    flask_clients.pop(session[constants.SESSION])
    session.pop(constants.SESSION)
    return redirect(url_for('auth.login'))

@chat.route('/')
def index():
    return render_template('base.html')

@chat.route('/home')
def home():
    return render_template('home.html')

@chat.route('/chat')
def chatview():
    return render_template('chat.html')

@chat.route('/get_name')
def get_name():
    sesion = session.get(constants.SESSION)
    name = flask_clients[sesion]["name"]
    return {"name": name}
