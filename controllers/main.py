# -*- coding: UTF-8 -*-
from flask import Blueprint, request, redirect, abort, url_for
from flask import render_template as tpl, jsonify

main_bp = Blueprint('main', __name__, template_folder='../templates/main')


@main_bp.route('/', methods=['GET'])
def index():
    return tpl("form.html")