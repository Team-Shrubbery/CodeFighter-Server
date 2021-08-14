import socketio
from faker import Faker
from time import time, sleep

fake = Faker("en_US")

# -------------- Will trigger Global Namespace in Server ----------
sio = socketio.Client()


@sio.event
def connect():
    print("Player 1-A Connected")
    sio.emit("message from client", "Player 1-A")


@sio.event
def my_message(data):
    print("message received with ", data)
    sio.emit("my response", "A listener that was triggered by response")


@sio.event
def move(data):
    print("We received this move from the other player: ", data)


@sio.event
def disconnect():
    print("disconnected from server")


sio.connect("http://localhost:8000")

# while True:
#     sio.emit("move", "right")
#     sleep(1)

# sio.wait()
