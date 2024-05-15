import socket
from flask import Flask, render_template, Response, request

from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", namespace="/")
    
@app.route('/')
def mostrar_informacion():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')
    data = 'Hola desde el servidor'
    print(data)
    socketio.emit('event', data)    

if __name__ == '__main__':    
    socketio.run(app, debug=True)
