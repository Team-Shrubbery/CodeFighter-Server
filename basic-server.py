import socketio

# When websockets arent used, multi threaded web server is needed
# run gunicorn -threads 50 server:app
# Without websockets, this forces clients to do a polling cycle to get events
# We will try eventlet
# gunicorn -k eventlet -w 1 --reload basic-server:app
# create requirement.txt >> poetry export -f requirements.txt --output requirements.txt

sio = socketio.Server()
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print("sid: ", sid)
    print("environ: ", environ)
    sio.emit("greeting", "Hello from server!")


@sio.event
def message(sid, data):
    print("sid: ", sid)
    print("message: ", message)


@sio.event
def disconnect(sid):
    print("Disconneted sid: ", sid)
