#!/usr/bin/env python
from flask import Flask
import config
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='')
api = Api(app)
configuration = config.DevelopmentConfig()
app.config.from_object(configuration)
db = SQLAlchemy(app)

from app import routes
from app import models

routes.initialize()
models.initialize()
