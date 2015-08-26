#!/usr/bin/env python
"""
docstring settings

"""
from os.path import join, dirname, abspath
from dotenv import load_dotenv
import os

dotenv_path = abspath(join(dirname(__file__), '../env', '.env'))
load_dotenv(dotenv_path)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    'testing': TestingConfig
}
