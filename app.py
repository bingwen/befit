#-*- coding: utf-8 -*-
from flask import url_for, redirect

from factory import create_app
from urls import register_blueprint
from config import config_object


app = create_app(config_object)


@app.route('/')
def index():
    return redirect(url_for("main.index"))

# urls
register_blueprint(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
