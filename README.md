# CodeFighter Socket IO Server

## Authors

Davee Sok, Prabin Singh, Kassie Bradshaw, Glen Clark, Michael Ryan

## Links & Resources

- [Deployed URL](https://codefighter-server.herokuapp.com/)
- [Code Fighter Game Repository](https://github.com/Team-Shrubbery/CodeFighter)
- [Python Socket IO docs](https://python-socketio.readthedocs.io/en/latest/intro.html)
- [Eventlet/Gunicorn Issues](https://github.com/eventlet/eventlet/issues/702)
- [Miguel Grinberge Youtube](https://www.youtube.com/playlist?list=PLCuWRxjbgFnPZTBMYbz9UNGvTLNggRMjb)

## Overview

Gunicorn server with socketio functionality providing real-time bidirectional event-based communication to a multiplayer game.

## Tools & Dependencies

- Gunicorn
- Eventlet
- Python Socket IO

## Getting Started

- Clone down this repo
- Install dependencies
- To start server, enter into command line:  
  `gunicorn -k eventlet -w 1 --reload server:app`
