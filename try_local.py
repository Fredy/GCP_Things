#!/usr/bin/env python

from flask import Flask, request
from main import image_borders

if __name__ == "__main__":
    app = Flask(__name__)


    @app.route('/')
    def index():
        return image_borders(request)


    app.run('127.0.0.1', 8002, debug=True)
