#-*- coding: UTF-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from app import app
from libs.db import db
db.drop_all()
db.create_all()
