import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'QuixoticMeowth~#7213'
    SEND_FILE_MAX_AGE_DEFAULT = os.environ.get('SEND_FILE_MAX_AGE_DEFAULT') or 0

