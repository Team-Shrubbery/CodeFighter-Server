import socketio
from faker import Faker
from time import time, sleep
import random

fake = Faker("en_US")

# -------------- Will trigger Global Namespace in Server ----------
sio = socketio.Client()


@sio.event
def connect():
    print("Player 1 Connected")
    sio.emit("message from client", "Player 1")


@sio.event
def my_message(data):
    print("message received with ", data)
    sio.emit("my response", "A listener that was triggered by response")


@sio.event
def disconnect():
    print("disconnected from server")


sio.connect("http://localhost:8000")

while True:
    sio.emit(
        "move",
        fake.name(),
    )
    sleep(2)

# sio.wait()
