#!/usr/bin/python
from flup.server.fcgi import WSGIServer
# from befit import app
# import app
from app import app

if __name__ == '__main__':
    WSGIServer(app, bindAddress='/tmp/befit-fcgi.sock').run()