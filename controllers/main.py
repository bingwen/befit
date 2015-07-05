# # -*- coding: UTF-8 -*-
# import datetime
# import time
# import hashlib
#
# from flask import Blueprint, request, abort, url_for, redirect, g
# from flask import render_template as tpl
# from flask import current_app as app
# from models.info import Info
#
# main_bp = Blueprint('main', __name__, template_folder='../templates/main')
# item_names = {
#     'neck': u"颈围",
#     'shoulder': u"肩宽",
#     'arm_length': u"臂长",
#     'arm_width': u"上臂围",
#     'chest': u"胸围",
#     'waist': u"腰围",
#     'butt': u"臀围",
#     'leg_length': u"腿长",
#     'leg_width': u"大腿围"
# }
# item_header_names = {
#     'neck': u"量颈围 9/9",
#     'shoulder': u"量肩宽 6/9",
#     'arm_length': u"量臂长 7/9",
#     'arm_width': u"量上臂围 8/9",
#     'chest': u"量胸围 1/9",
#     'waist': u"量腰围 2/9",
#     'butt': u"量臀围 3/9",
#     'leg_length': u"量腿长 4/9",
#     'leg_width': u"量大腿围 5/9"
# }
# items = ['chest', 'waist', 'butt', 'leg_length', 'leg_width', 'shoulder', 'arm_length', 'arm_width', 'neck']
# items_length = len(items)
#
#
# @main_bp.route('/', methods=['GET'])
# def index():
#     return tpl("show.html", data=request.url)
#     # if g.info.height and g.info.birthday:
#     #     return redirect(url_for('main.user_info', weixin_id=g.info.weixin_id))
#     # else:
#     #     return redirect(url_for('main.slide'))
#
#
# @main_bp.route('/address', methods=['GET'])
# def address():
#     time_ = int(time.time())
#     data = 'accesstoken=' + g.identification[2] + '&appid=' + app.config['WEIXIN_AK'] + '&noncestr=12345&timestamp=' + str(time_) + '&url=' + request.url
#     addrSign = hashlib.sha1(data).hexdigest()
#     return tpl("address.html", appID=app.config['WEIXIN_AK'], addrSign=addrSign, data=data, time_=time_)
#
#
# @main_bp.route('/slide', methods=['GET'])
# def slide():
#     return tpl("slide.html")
#
#
# @main_bp.route('/base/', methods=['GET', 'POST'])
# def base_info():
#     if request.method == 'POST':
#         g.info.weixin_name = request.values.get('weixin_name')
#         g.info.sex = int(request.values.get('sex'))
#         g.info.height = int(request.values.get('height'))
#         g.info.weight = int(request.values.get('weight'))
#         g.info.birthday = datetime.datetime.strptime(request.values.get('birthday'), "%Y-%m-%d").date()
#         g.info.save()
#         return redirect(url_for("main.item_form", item='chest'))
#     return tpl("base_info.html")
#
#
# @main_bp.route('/<item>/', methods=['GET', 'POST'])
# def item_form(item):
#     if not item in items:
#         abort(404)
#     if request.method == 'POST':
#         setattr(g.info, item, int(request.values.get('item_value')))
#         g.info.save()
#
#         item_index = items.index(item)
#         item_action = request.values.get('item_action', 'next')
#         if item_action == 'next':
#             if item_index < items_length - 1:
#                 return redirect(url_for('main.item_form', item=items[item_index + 1]))
#             else:
#                 return redirect(url_for('main.user_info', weixin_id=g.info.weixin_id))
#         elif item_action == 'pre':
#             if item_index > 0:
#                 return redirect(url_for('main.item_form', item=items[item_index - 1]))
#             else:
#                 return redirect(url_for('main.base_info'))
#         elif item_action == 'report':
#             return redirect(url_for('main.mine'))
#     item_value = getattr(g.info, item) or 80
#     return tpl("item.html", item=item,
#                item_name=item_names[item],
#                item_header_name=item_header_names[item],
#                item_value=item_value)
#
#
# @main_bp.route('/mine/', methods=['GET'])
# def mine():
#     if g.info.height and g.info.birthday and g.info.weixin_name:
#         return redirect(url_for('main.user_info', weixin_id=g.info.weixin_id))
#     else:
#         return redirect(url_for('main.base_info'))
#
#
# @main_bp.route('/u/<weixin_id>/', methods=['GET'])
# def user_info(weixin_id):
#     info = Info.get_by_weixin(weixin_id)
#     if not info:
#         abort(404)
#     if not info.height or not info.birthday:
#         return redirect(url_for('main.base_info'))
#     return tpl("user_info.html", info=info)
#
#
# @main_bp.route('/u/<weixin_id>/compare', methods=['GET'])
# def user_compare(weixin_id):
#     info = Info.get_by_weixin(weixin_id)
#     if not info:
#         abort(404)
#     if not info.height or not info.birthday:
#         return redirect(url_for('main.base_info'))
#     return tpl("user_compare.html", info=info)
