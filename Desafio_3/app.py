# Nesse desafio, vamos iniciar um projeto com Flask e Flask-SocketIO que funcionará como um chat em tempo real de forma simplificada.

# Criar a rota para renderizar o arquivo index.html e a função do socketio que será responsável
# por verificar as mensagens enviadas no "chat" que criaremos.
from flask import Flask, render_template    
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/comumnication", methods=['GET'])
def create_comumnication():

    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    message = msg
    
    if not message.strip() or message == 'porra':
        emit('message', 'message invalid')
        return
    
    print('Received message:', msg)
    emit('message', f'Message: {msg}')

if __name__ == '__main__':
    socketio.run(app, debug=True)
