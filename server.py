# run this in the terminal to start server
# >>>>>> gunicorn --threads 50 server:app
# gunicorn -k eventlet -w 1 --reload server:app
# ----------------------------------
# the code about uses gunicorn to start the server
# it uses 50 threads
# nameOfFile : the app variable
import socketio


# import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

# eventlet.wsgi.server(eventlet.listen(("", 8000)), app)


players = []


@sio.event
def connect(sid, environ):
    print("A New Player Connected: ", sid)
    if len(players) == 0:
        sio.emit("position", {"result": "Player 1"}, room=sid)
        print("We have a player1")
    if len(players) == 1:
        sio.emit("position", {"result": "Player 2"}, room=sid)
        print("We have a player2")

    players.append(sid)
    sio.enter_room(sid, "game room")
    print("A new player entered game room")


@sio.event
def move(sid, data):
    print("MOVE from client: ", data)
    if len(players) > 1:
        sio.emit("receive", data, room="game room", skip_sid=sid)


@sio.event
def disconnect(sid):
    print("Disconnected SID >> ", sid)
    players.remove(sid)
    print("This is now the list: ", players)
