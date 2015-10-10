from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

# settings config init
app.config.from_object('application.settings')
