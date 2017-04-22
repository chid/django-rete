import os, sys
PROJECT_DIR = os.path.dirname(__file__)
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        # Don't do this. It dramatically slows down the test.
#        'NAME': '/tmp/database_files.db',
#        'TEST_NAME': '/tmp/database_files.db',
    }
}
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.sites',
    'triple',
    'rete',
]

from django.utils.crypto import get_random_string
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, chars)