#-*- coding: utf-8 -*-
from flask import url_for, redirect, request, g
from flask.ext.login import LoginManager, current_user, login_user

from factory import create_app
from urls import register_blueprint
from config import config_object


app = create_app(config_object)


login_manager = LoginManager()
login_manager.login_message = None
login_manager.init_app(app)
login_manager.login_view = "user.login"


@login_manager.user_loader
def load_user(userid):
    from models.info import Info
    return Info.get_by_weixin(userid)


@app.before_request
def request_user():
    if current_user and current_user.is_authenticated():
        g.user = current_user
    else:
        code = request.values.get('code')
        if code:
            from models.info import Info
            from libs.weixin import get_weixin_user_openid
            openid = get_weixin_user_openid(code)
            info = Info.get_by_weixin(openid)
            if not info:
                info = Info.add(openid)
            login_user(info)
        else:
            from libs.weixin import get_weixin_login_url
            login_url = get_weixin_login_url(request.url)
            return redirect(login_url)


@app.route('/')
def index():
    return redirect(url_for("main.index"))

# urls
register_blueprint(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
