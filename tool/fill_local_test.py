#-*- coding: UTF-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from app import app
from libs.db import db
from models.user import User

user = User.add(weixin_id='local_test', weixin_name='local_test', weixin_union='weixin_union', phone_number='12345678901')
