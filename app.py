#-*- coding: utf-8 -*-
from flask import url_for, redirect, request, g, session
from flask.ext.login import LoginManager, current_user, login_user

from factory import create_app
from urls import register_blueprint
from config import config_object

from models.user import User

app = create_app(config_object)


login_manager = LoginManager()
login_manager.login_message = None
login_manager.init_app(app)
login_manager.login_view = "user.login"


@login_manager.user_loader
def load_user(userid):
    return User.get_by_id(userid) or None


@app.before_request
def request_user():
    if current_user and current_user.is_authenticated():
        g.user = current_user
    elif request.path.startswith(u'/user/signin') or request.path.startswith(u'/static/'):
        pass
    elif request.remote_addr == '127.0.0.1':
        g.user = User.get_by_id('local_test')
        login_user(g.user)
        # return redirect(url_for("user.figure", next=request.url))
    else:
        code = request.values.get('code')
        if code:
            from libs.weixin import get_weixin_user_identification
            identification = get_weixin_user_identification(code)
            if identification:
                session['identification'] = identification
                if request.path.startswith(u'/address'):
                    pass
                else:
                    user = User.get_by_id(session['identification']['openid'])
                    if not user:
                        return redirect(url_for("user.signin", next=request.url))
                    login_user(user)
                    g.user = user
            else:
                return u"微信登录失败啦"
        else:
            from libs.weixin import get_weixin_login_url
            login_url = get_weixin_login_url(request.url)
            return redirect(login_url)


@app.route('/')
def index():
    return redirect(url_for("main.index"))


@app.route('/figure')
def figure():
    return redirect(url_for("user.figure"))

# urls
register_blueprint(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
