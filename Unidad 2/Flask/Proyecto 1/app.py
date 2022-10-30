
from flask import Flask,render_template,request,jsonify,session,url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
import logging
app = Flask(__name__)

app.secret_key="llave_secreta"

logging.basicConfig(filename="error.log",level=logging.DEBUG)

@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ha hecho sesion {session["username"]}'
    else:
        return redirect(url_for('login'))

@app.route('/login' ,methods=['GET','POST'])
def login():
    if request.method == "POST":
        usuario = request.form['username']
        session['username']=usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'saludos {nombre}'

@app.route('/edad/<int:edad>', methods=['GET'])
def edad(edad):
    return f'Edad {edad}'

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html',error=error) , 404

@app.route("/juego", methods=["POST"])
def insertarJuego():
    token  = request.headers.get('token')
    app.logger.debug("TOKEN" + token)
    info = request.get_json()
    nombre = info["nombre"]
    precio = info["precio"]
    calificacion = info["calificacion"]
    return f'Juego {nombre} {precio} {calificacion}'

@app.route('/juego/<int:id>')
def mostrarJuego(id):
    valores = {"nombre":"unnombre","precio":90.0,"calificacion":90,"id":id}
    return jsonify(valores)    


