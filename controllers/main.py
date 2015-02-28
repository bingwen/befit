# -*- coding: UTF-8 -*-
import datetime
from flask import Blueprint, request, abort, url_for, redirect, g
from flask import render_template as tpl
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
items = ['neck', 'shoulder', 'arm_length', 'arm_width', 'chest', 'waist', 'butt', 'leg_length', 'leg_width']
items_length = len(items)


@main_bp.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.base_info'))


@main_bp.route('/base/', methods=['GET', 'POST'])
def base_info():
    if request.method == 'POST':
        g.info.weixin_name = request.values.get('weixin_name')
        g.info.sex = int(request.values.get('sex'))
        g.info.height = int(request.values.get('height'))
        g.info.weight = int(request.values.get('weight'))
        g.info.birthday = datetime.datetime.strptime(request.values.get('birthday'), "%Y-%m-%d").date()
        g.info.save()
        return redirect(url_for("main.item_form", item='neck'))
    return tpl("base_info.html")


@main_bp.route('/<item>/', methods=['GET', 'POST'])
def item_form(item):
    if not item in items:
        abort(404)
    if request.method == 'POST':
        setattr(g.info, item, int(request.values.get('item_value')))
        g.info.save()
        item_index = items.index(item)
        item_action = request.values.get('item_action', 'next')
        if item_action == 'next':
            if item_index < items_length - 1:
                return redirect(url_for('main.item_form', item=items[item_index + 1]))
            else:
                return redirect(url_for('main.user_info', weixin_id=g.info.weixin_id))
        elif item_action == 'pre':
            if item_index > 0:
                return redirect(url_for('main.item_form', item=items[item_index - 1]))
            else:
                return redirect(url_for('main.base_info'))
    item_value = getattr(g.info, item) or 80
    return tpl("item.html", item=item, item_name=item_names[item], item_value=item_value)


@main_bp.route('/u/<weixin_id>/', methods=['GET'])
def user_info(weixin_id):
    info = Info.get_by_weixin(weixin_id)
    if not info:
        abort(404)
    return tpl("user_info.html", info=info)
