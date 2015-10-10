from application.app import app

from mongoengine import *
import datetime

# Mongo DB instance
# connect(app.config['MONGODB_SETTINGS'])
connect("omprakashp_db", host="127.0.0.1", port=27017)

class User(Document):
	"""docstring for User"""
	name = StringField(required=True)
	email = StringField(required=True, max_length=100, unique=True)
	password = StringField(required=True, min_length=6, max_length=32)

