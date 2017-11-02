from flask_mongoengine.wtf import model_form
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Test(db.Document):
    email = db.StringField()
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
