#-*- coding: UTF-8 -*-
import datetime
from . import db, BaseModelMixin


class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'

    weixin_id = db.Column(db.String(100), primary_key=True)
    weixin_name = db.Column(db.String(100))
    weixin_union = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))

    def __init__(self, weixin_id, weixin_name, weixin_union, phone_number):
        self.weixin_id = weixin_id
        self.weixin_name = weixin_name
        self.weixin_union = weixin_union
        self.phone_number = phone_number

    @classmethod
    def get_by_id(cls, weixin_id):
        return cls.query.filter_by(weixin_id=weixin_id).first()

    @classmethod
    def get_by_union(cls, weixin_union):
        return cls.query.filter_by(weixin_union=weixin_union).first()

    def is_active(self):
        return self.weixin_id

    def is_authenticated(self):
        return self.weixin_id

    def get_id(self):
        return self.weixin_id
