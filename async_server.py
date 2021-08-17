# run this in the terminal to start server
# >>>>>> gunicorn --threads 50 server:app
# gunicorn -k eventlet -w 1 --reload server:app
# uvicorn async_server:app
# ----------------------------------
# the code about uses gunicorn to start the server
# it uses 50 threads
# nameOfFile : the app variable
import socketio


# import eventlet

sio = socketio.AsyncServer(async_mode="asgi")
app = socketio.ASGIApp(sio)


players = []


@sio.event
async def connect(sid, environ):
    print("A New Player Connected: ", sid)
    if len(players) == 0:
        await sio.emit("position", "Player1", room=sid)
        print("We have a player1")
    if len(players) == 1:
        await sio.emit("position", "Player2", room=sid)
        print("We have a player2")

    players.append(sid)
    sio.enter_room(sid, "game room")
    print("A new player entered game room")


@sio.event
async def move(sid, data):
    print("MOVE from client: ", data)
    if len(players) > 1:
        await sio.emit("receive", data, room="game room", skip_sid=sid)


@sio.event
async def disconnect(sid):
    print("Disconnected SID >> ", sid)
    players.remove(sid)
    print("This is now the list: ", players)
