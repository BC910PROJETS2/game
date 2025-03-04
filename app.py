from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

players = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    players[username] = request.sid
    emit('player_joined', {'username': username}, broadcast=True)

@socketio.on('guess')
def handle_guess(data):
    guess = data['guess']
    emit('new_guess', {'guess': guess}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
