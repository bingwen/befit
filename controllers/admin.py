# -*- coding: UTF-8 -*-
import StringIO
import unicodecsv
from functools import wraps
from flask import Blueprint, Response, make_response, request
from flask import render_template as tpl
from models.info import Info

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'roy' and password == 'befit'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response('Could not verify your access level for that URL.\nYou have to login with proper credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/', methods=['GET'])
@requires_auth
def index():
    return tpl("admin.html", infos=Info.all())


@admin_bp.route('/download', methods=['GET'])
@requires_auth
def download():
    si = StringIO.StringIO()
    cw = unicodecsv.writer(si)
    cw.writerow([u"Name", u"出生年月", u"性别", u"身高", u"体重", u"颈围",
                 u"肩宽", u"臂长", u"臂围", u"胸围", u"腰围", u"臀围",
                 u"腿长", u"大腿围"])
    for info in Info.all():
        cw.writerow(info.str_infos)
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=befit.csv"
    output.headers["Content-type"] = "text/csv"
    return output
