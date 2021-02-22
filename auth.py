from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ioserver import flask_clients
import constants

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=["GET", "POST"])
def login():
    if(session.get(constants.SESSION)):
        return redirect("/")
    if(request.method == "POST"):
        nick = request.form["nick"]
        if(nick not in flask_clients):
            session[constants.SESSION] = nick
            flask_clients[nick] = {"name": nick}
            return redirect(url_for('auth.login'))
        flash("El nombre de usuario ya se encuentra en uso; probá con otro nickname!!")
    return render_template('login.html')
