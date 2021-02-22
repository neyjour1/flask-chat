# Python Online Chat
un simple chat de browser

Server -> `Python3, Flask, flask-socketio`

Cliente -> browser (`HTML, CSS, JS, Bootstrap`, `socketio`) 

# Setup

1.  `git clone https://github.com/neyjour1/flask-chat.git`
2.  Estando en el directorio: `py -m pip install -r requirements.txt`
3.  `py main.py`
4.  Abrir > [http://localhost:4004](http://localhost:4004/) 

## Uso

**ENDPOINTS**:
<code>
* Login (no hay registro) -> endpoint "/login"
* Chat (usa socketio) -> endpoint "/chat" (*requiere session*)
* Home (no hay nada útil) -> endpoint "/home" (*requiere session*)
* Base (no hay nada útil) -> endpoint "/" (*requiere session*)
* get_name (se usa para fetchear el username) -> endpoint "/get_name" (*requiere session* **creo, no me acuerdo XD**)
</code>

al intentar acceder a un endpoint que **requiere session**, si no estas logueado, se te redirecciona a /login

## Notas
-   PORT=4004 (default); se puede cambiar en `constants.py`
-   HOST='0.0.0.0' (default: localhost); también se puede modificar desde `constants.py`
