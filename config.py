# -*- coding: utf-8 -*-


import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id/<username>'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com/<username>'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'myStevens', 'url': 'http://mystevens.stevens.edu/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['tarik.kdiry@gmail.com']

# pagination
POSTS_PER_PAGE = 5

# For search results
MAX_SEARCH_RESULTS = 50

# languages offered
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}
