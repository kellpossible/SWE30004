import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'changed-this-needs-to-be'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///test.db')


class ProductionConfig(Config):
    DEBUG = False
    SERVER_NAME = '127.0.0.1:5000'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SERVER_NAME = '0.0.0.0:2227'


class TestingConfig(Config):
    TESTING = True
