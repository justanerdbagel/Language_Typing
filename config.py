import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'QuixoticMeowth~#7213'
    SEND_FILE_MAX_AGE_DEFAULT = os.environ.get('SEND_FILE_MAX_AGE_DEFAULT') or 0
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
