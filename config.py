import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Used to protect against CSRF acttacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'INSERT SECRET KEY'
    # database configuration
    SQLALCHEMY_DATABASE_URI = 'postgresql://USERNAME:PASSWORD@localhost/catalog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
