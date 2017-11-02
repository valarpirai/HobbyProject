from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView

from .models import db, Test

app = Flask(__name__)
flask_app = app

admin = admin.Admin(app, 'Example: MongoEngine')
admin.add_view(ModelView(Test))
# flask_app.config.from_pyfile('config.cfg')

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://admin:abc123@127.0.0.1:27017/test'
# }

app.debug = True

app.config['MONGODB_DB'] = 'project1'
app.config['MONGODB_HOST'] = 'mongodb://127.0.0.1:27017/'
# app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'hello'
app.config['MONGODB_PASSWORD'] = 'world'


db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)


@app.route('/')
def index():
    ross = Test(email='ross@example.com')
    ross.first_name = 'Ross'
    ross.last_name = 'Lawley'
    ross.save()
    return '<a href="/admin/">Click me to get to Admin!</a>'


@app.route('/hello')
def hello():
    return 'Hello, World'
