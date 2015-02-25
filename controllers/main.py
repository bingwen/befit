# -*- coding: UTF-8 -*-
from flask import Blueprint, request, redirect, abort, url_for
from flask import render_template as tpl, jsonify

from models.info import Info

main_bp = Blueprint('main', __name__, template_folder='../templates/main')
item_names = {
    'neck': u"颈围",
    'shoulder': u"肩宽",
    'arm_length': u"臂长",
    'arm_width': u"臂围",
    'chest': u"胸围",
    'waist': u"腰围",
    'butt': u"臀围",
    'leg_length': u"腿长",
    'leg_width': u"腿围"
}


@main_bp.route('/', methods=['GET'])
def index():
    return tpl("index.html")


@main_bp.route('/<item>/', methods=['GET', 'POST'])
def item_form(item):
    if not item in item_names.keys():
        abort(404)
    return tpl("item.html", item=item, item_name=item_names[item])
