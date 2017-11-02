from flask import Flask
from flask_mongoengine import MongoEngine

flask_app = Flask(__name__)
app = flask_app
# flask_app.config.from_pyfile('config.cfg')

app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': 'mongodb://admin:abc123@127.0.0.1:27017/'
}

db = MongoEngine(flask_app)

@app.route('/')
def index():
    return 'Index page'


@app.route('/hello')
def hello():
    return 'Hello, World'
