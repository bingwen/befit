# -*- coding: UTF-8 -*-
import urllib2
import urllib
import json

from flask import Blueprint, request, abort, url_for, redirect, session, g
from flask import render_template as tpl, jsonify
from flask.ext.login import login_user
from flask import current_app as app

from models.user import User
from models.figure import Figure

user_bp = Blueprint('user', __name__, template_folder='../templates/user')


@user_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        code = request.args.get('signin_code', 0, type=str)
        phone_number = request.args.get('phone_number', "123456789", type=str)
        if code == 'get_code':
            session['code'] = '1234'
            return jsonify({'status': 'ok'})
        return tpl('register.html')
    elif request.method == 'POST':
        code = request.form.get('signin_code', 0, type=str)
        phone_number = request.form.get('phone_number', 0, type=str)
        if 'code' in session and session['code'] == code:
            user = User.add(weixin_id=session['identification']['openid'],
                            weixin_name='test',
                            weixin_union=session['identification']['unionid'],
                            phone_number=phone_number)
            login_user(user)
            return redirect(request.args.get("next", "/"))
        return tpl('register.html', error=u'验证错误')


@user_bp.route('/figure', methods=['GET', 'POST'])
def figure():
    if request.method == 'GET':
        get_url = app.config['API_DOMIN'] + 'get_figure_by_unionid/' + g.user.weixin_union
        response = urllib2.urlopen(get_url)
        html = response.read()
        json_info = json.loads(html)
        if json_info.get('status') != 404:
            figure = Figure(
                height=json_info.get('height'),
                neck=json_info.get('neck'),
                waist=json_info.get('waist'),
                arm_length=json_info.get('arm_length'),
                leg_length=json_info.get('leg_length'),
                chest=json_info.get('chest'),
                butt=json_info.get('butt'),
                leg_width=json_info.get('leg_width'),
                arm_width=json_info.get('arm_width'),
                shoulder=json_info.get('shoulder'))
        else:
            figure = Figure(
                height=50,
                neck=50,
                waist=50,
                arm_length=50,
                leg_length=50,
                chest=50,
                butt=50,
                leg_width=50,
                arm_width=50,
                shoulder=50)
        return tpl('figure.html', figure=figure)
    elif request.method == 'POST':
        print request.form
        figure = Figure(
            height=request.form.get('height', 0, type=int),
            neck=request.form.get('neck', 0, type=int),
            waist=request.form.get('waist', 0, type=int),
            arm_length=request.form.get('arm_length', 0, type=int),
            leg_length=request.form.get('leg_length', 0, type=int),
            chest=request.form.get('chest', 0, type=int),
            butt=request.form.get('butt', 0, type=int),
            leg_width=request.form.get('leg_width', 0, type=int),
            arm_width=request.form.get('arm_width', 0, type=int),
            shoulder=request.form.get('shoulder', 0, type=int))
        post_url = app.config['API_DOMIN'] + 'save_figure_by_unionid/' + g.user.weixin_union
        req = urllib2.Request(post_url)
        print figure.__dict__
        data = urllib.urlencode(figure.__dict__)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, data)
        if json.loads(response.read()).get('status') == 200:
            return tpl('figure.html', figure=figure, status='success')
        else:
            return tpl('figure.html', figure=figure, status='fail')
