from flask_mongoengine.wtf import model_form
from flask_admin.contrib.mongoengine import ModelView
from flask_admin.form import rules
import flask_admin as admin
from flask_mongoengine import MongoEngine

import datetime

db = MongoEngine()

class Test(db.Document):
    email = db.StringField()
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
