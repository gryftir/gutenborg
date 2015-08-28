#!/usr/bin/env python
from flask import Flask
import config
# from flask_restful import Api


app = Flask(__name__, static_url_path='')
# api = Api(app)
configuration = config.DevelopmentConfig()
app.config.from_object(configuration)

from app import routes

routes.initialize()
