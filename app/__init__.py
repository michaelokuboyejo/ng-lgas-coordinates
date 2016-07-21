
from flask.ext.pymongo import PyMongo

__author__ = 'michaelokuboyejo'

from flask import Flask
from endpoints.controllers import endpoints as endpoints_module


application = Flask(__name__)

application.register_blueprint(endpoints_module)
