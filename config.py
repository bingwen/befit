class Config(object):
    SECRET_KEY = 'your key'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://vagrant:vagrant@localhost/befit'

    SENTRY_DSN = ''
    DOMAIN = ''


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class DevelopmentConfig(Config):
    """Use local_config overwrite this"""
    pass

config_object = 'config.DevelopmentConfig'

try:
    from local_config import *
except ImportError:
    pass
