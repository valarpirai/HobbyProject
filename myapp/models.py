from flask_mongoengine.wtf import model_form
from flask_admin.contrib.mongoengine import ModelView
from flask_admin.form import rules
import flask_admin as admin
from flask_mongoengine import MongoEngine

import datetime

db = MongoEngine()

class WebResult(db.Document):
    search_str = db.StringField(max_length=100)
    data = db.DictField()
    created = db.DateTimeField(default=datetime.datetime.now)
    modified = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(WebResult, self).save(*args, **kwargs)
