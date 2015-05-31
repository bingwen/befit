# -*- coding: UTF-8 -*-
from flask import Blueprint, request, abort, url_for, redirect, g, session
from flask import render_template as tpl, jsonify

user_bp = Blueprint('user', __name__, template_folder='../templates/user')


@user_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        code = request.form.get('signin_code', 0, type=str)
        if session['user_code'] and code == session['user_code']:
            return redirect(request.args.get("next", "/"))
        return tpl('signin.html', error=u'验证错误')
    return tpl('signin.html')


@user_bp.route('/get_code', methods=['GET'])
def get_code():
    session['user_code'] = '1234'
    return jsonify({'code': '1234'})

@user_bp.route('/figure', methods=['GET', 'POST'])
def figure():
    return tpl('figure.html')
