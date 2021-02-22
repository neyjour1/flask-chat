import os
# SESSION / SECRET_KEY
SESSION = "username"
SECRET_KEY = "hellothisisasecretkeyuwontguessitxd"
SESSION_LIFETIME_DAYS = 31

# SERVER
PORT = 4004
HOST = os.environ.get('IP') or '0.0.0.0' # cambiar el 'HOST' '0.0.0.0' por la IPv4 local ('ipconfig' en windows cmd) y, opcionalmente, forwardear el puerto 'PORT' para runnear el sv públicamente
