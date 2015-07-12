#-*- coding: UTF-8 -*-
import datetime
from . import db, BaseModelMixin


class AuthCode(db.Model, BaseModelMixin):
    __tablename__ = 'auth_code'

    weixin_id = db.Column(db.String(100), primary_key=True)
    code = db.Column(db.String(6))
    expiration = db.Column(db.DateTime)

    def __init__(self, weixin_id, code):
        self.weixin_id = weixin_id
        self.code = code
        self.expiration = datetime.datetime.now() + datetime.timedelta(minutes=2)

    @classmethod
    def is_authenticated(cls, weixin_id, code):
        ac = cls.query.filter_by(weixin_id=weixin_id).first()
        if ac and ac.expiration > datetime.datetime.now() and ac.code == code:
            cls.delete(ac)
            return True
        return False
