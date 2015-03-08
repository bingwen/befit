#-*- coding: UTF-8 -*-
import datetime
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
    def age(self):
        return (datetime.date.today() - self.birthday).days // 365

    @property
    def biaozhun_neck(self):
        if self.sex == 1:
            return int(self.height * 0.2 + (self.age - 30) * 0)
        else:
            return int(self.height * 0.2 + (self.age - 35) * 0)

    @property
    def biaozhun_shoulder(self):
        if self.sex == 1:
            return int(self.height * 0.23 + (self.age - 30) * 0)
        else:
            return int(self.height * 0.25 + (self.age - 35) * 0)

    @property
    def biaozhun_arm_length(self):
        if self.sex == 1:
            return int(self.height * 0.31 + (self.age - 30) * 0)
        else:
            return int(self.height * 0.31 + (self.age - 35) * 0)

    @property
    def biaozhun_arm_width(self):
        if self.sex == 1:
            return int(self.height * 0.14 + (self.age - 30) * 0.1)
        else:
            return int(self.height * 0.16 + (self.age - 35) * 0.1)

    @property
    def biaozhun_chest(self):
        if self.sex == 1:
            return int(self.height * 0.51 + (self.age - 30) * 0)
        else:
            return int(self.height * 0.48 + (self.age - 35) * 0)

    @property
    def biaozhun_waist(self):
        if self.sex == 1:
            return int(self.height * 0.38 + (self.age - 30) * 0.1)
        else:
            return int(self.height * 0.43 + (self.age - 35) * 0.15)

    @property
    def biaozhun_butt(self):
        if self.sex == 1:
            return int(self.height * 0.53 + (self.age - 30) * 0.15)
        else:
            return int(self.height * 0.51 + (self.age - 35) * 0.1)

    @property
    def biaozhun_leg_width(self):
        if self.sex == 1:
            return int(self.height * 0.29 + (self.age - 30) * 0.15)
        else:
            return int(self.height * 0.3 + (self.age - 35) * 0.1)

    @property
    def biaozhun_leg_length(self):
        if self.sex == 1:
            return int(self.height * 0.45 + (self.age - 30) * 0)
        else:
            return int(self.height * 0.44 + (self.age - 35) * 0)

    @property
    def biaozhun_weight(self):
        if self.sex == 1:
            return int((self.height - 95) * 0.7 + (self.age - 30) * 0.3)
        else:
            return int((self.height - 95) * 0.8 + (self.age - 35) * 0.3)

    @property
    def str_infos(self):
        return (self.weixin_name or "",
                str(self.birthday) or "",
                self.sex_name,
                str(self.height),
                str(self.weight),
                str(self.neck),
                str(self.shoulder),
                str(self.arm_length),
                str(self.arm_width),
                str(self.chest),
                str(self.waist),
                str(self.butt),
                str(self.leg_width),
                str(self.leg_length))
