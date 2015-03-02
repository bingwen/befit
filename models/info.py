#-*- coding: UTF-8 -*-
from . import db, BaseModelMixin


class Info(db.Model, BaseModelMixin):
    __tablename__ = 'info'

    id = db.Column(db.Integer, primary_key=True)
    weixin_id = db.Column(db.String(100))
    weixin_name = db.Column(db.String(100))
    weixin_avatar = db.Column(db.String(100))

    neck = db.Column(db.Integer)
    shoulder = db.Column(db.Integer)
    arm_length = db.Column(db.Integer)
    arm_width = db.Column(db.Integer)
    chest = db.Column(db.Integer)
    waist = db.Column(db.Integer)
    butt = db.Column(db.Integer)
    leg_width = db.Column(db.Integer)
    leg_length = db.Column(db.Integer)

    birthday = db.Column(db.Date)
    sex = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    def __init__(self, weixin_id):
        self.weixin_id = weixin_id
        self.neck = 0
        self.shoulder = 0
        self.arm_length = 0
        self.arm_width = 0
        self.chest = 0
        self.waist = 0
        self.butt = 0
        self.leg_width = 0
        self.leg_length = 0
        self.height = 0
        self.weight = 0

    @property
    def sex_name(self):
        return u"女" if self.sex == 1 else u"男"

    @classmethod
    def get_by_weixin(cls, weixin_id):
        return cls.query.filter_by(weixin_id=weixin_id).first()

    def is_active(self):
        return self.weixin_id

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.weixin_id

    def get_id(self):
        return self.weixin_id

    @property
    def biaozhun_neck(self):
        return 80

    @property
    def biaozhun_shoulder(self):
        return 80

    @property
    def biaozhun_arm_length(self):
        return 80

    @property
    def biaozhun_arm_width(self):
        return 80

    @property
    def biaozhun_chest(self):
        return 80

    @property
    def biaozhun_waist(self):
        return 80

    @property
    def biaozhun_butt(self):
        return 80

    @property
    def biaozhun_leg_width(self):
        return 80

    @property
    def biaozhun_leg_length(self):
        return 80

    @property
    def biaozhun_weight(self):
        return 80
