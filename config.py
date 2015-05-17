class Config(object):
    SECRET_KEY = 'your key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://vagrant:vagrant@localhost/befit'

    SENTRY_DSN = ''
    DOMAIN = ''
    WEIXIN_AK = 'wx7ca8bfd8ecc57ddf'
    WEIXIN_SK = 'ae9b465ff9c2053aefce3da46c234486'


class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class DevelopmentConfig(Config):
    """Use local_config overwrite this"""
    pass

config_object = 'config.DevelopmentConfig'

try:
    from local_config import *
except ImportError:
    pass
