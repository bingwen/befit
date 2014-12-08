#-*- coding: UTF-8 -*-
import json
from sqlalchemy.ext.mutable import MutableDict

from . import db, BaseModelMixin


class Info(db.Model, BaseModelMixin):
    __tablename__ = 'info'

    id = db.Column(db.Integer, primary_key=True)
    weixin = db.Column(db.String(100))
    props = db.Column(MutableDict.as_mutable(db.PickleType(pickler=json)), default=None)

    def __init__(self, id, weixin):
        self.weixin = weixin
