from flask import Flask
from flask import render_template
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView

from .models import db, WebResult

app = Flask(__name__)
flask_app = app

admin = admin.Admin(app, 'Example: MongoEngine')
admin.add_view(ModelView(WebResult))
# flask_app.config.from_pyfile('config.cfg')

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://admin:abc123@127.0.0.1:27017/test'
# }

app.debug = True

app.config['MONGODB_DB'] = 'test'
app.config['MONGODB_HOST'] = 'mongodb://127.0.0.1:27017/'
# app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'hello'
app.config['MONGODB_PASSWORD'] = 'world'


db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)


@app.route('/', methods=['GET'])
def index():
    # ross = WebResult()
    # ross.search_str = 'dummy'
    # ross.save()
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/search/<search_str>', methods=['GET', 'POST'])
def search_web(search_str):
    # show the user profile for that user
    return 'User %s' % search_str

# A list page
# Get search query
# Post result page
