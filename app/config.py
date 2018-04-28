from pymongo import MongoClient
import os

mongo_uri = os.getenv('MONGO_URI')

mongo_client = MongoClient(mongo_uri)
