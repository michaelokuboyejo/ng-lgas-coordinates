from flask.ext.pymongo import PyMongo
from pymongo import MongoClient

__author__ = 'michaelokuboyejo'

mongo_db_name = 'ng_lga_coordinates'
mongo_db_uri = 'mongodb://ng_lga_coordinates:ng_lga_coordinates@ds011705.mlab.com:11705/ng_lga_coordinates'

mongoClient = MongoClient('mongodb://ng_lga_coordinates:ng_lga_coordinates@ds011705.mlab.com:11705/ng_lga_coordinates')


def dbServerHandShake(application_context):
    """

    :param application:
    :return: monogoClient Instance
    """
    application_context.config['MONGO_DBNAME'] = 'ng_lga_coordinates'
    application_context.config['MONGO_URI'] = 'mongodb://ng_lga_coordinates:ng_lga_coordinates@ds011705.mlab.com:11705/ng_lga_coordinates'
    return PyMongo(application_context)
