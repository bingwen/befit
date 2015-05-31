# -*- coding: UTF-8 -*-
from flask import Blueprint, request, abort, url_for, redirect, session
from flask import render_template as tpl, jsonify
from flask.ext.login import login_user

from models.user import User

user_bp = Blueprint('user', __name__, template_folder='../templates/user')


@user_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        code = request.args.get('signin_code', 0, type=str)
        phone_number = request.args.get('phone_number', "123456789", type=str)
        if code == 'get_code':
            session['code'] = '1234'
            return jsonify({'status': 'ok'})
        return tpl('signin.html')
    elif request.method == 'POST':
        code = request.form.get('signin_code', 0, type=str)
        phone_number = request.form.get('phone_number', 0, type=str)
        if 'code' in session and session['code'] == code:
            user = User.add(weixin_id=session['identification']['openid'],
                            weixin_name='test',
                            weixin_union=session['identification']['openid'],
                            phone_number=phone_number)
            login_user(user)
            return redirect(request.args.get("next", "/"))
        return tpl('signin.html', error=u'验证错误')


@user_bp.route('/figure', methods=['GET', 'POST'])
def figure():
    return tpl('figure.html')
