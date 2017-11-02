from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView

from .models import db, Test

app = Flask(__name__)
flask_app = app

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# admin.add_view(ModelView(Test, db.session))
# flask_app.config.from_pyfile('config.cfg')

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://admin:abc123@127.0.0.1:27017/test'
# }

app.debug = True

app.config['MONGODB_DB'] = 'project1'
app.config['MONGODB_HOST'] = '127.0.0.1'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'admin'
app.config['MONGODB_PASSWORD'] = 'abc123'


db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)


@app.route('/')
def index():
    ross = Test(email='ross@example.com')
    ross.first_name = 'Ross'
    ross.last_name = 'Lawley'
    ross.save()
    return 'Index page'


@app.route('/hello')
def hello():
    return 'Hello, World'
