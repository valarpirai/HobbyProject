from flask import Flask, render_template, request
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView

from .models import db, WebResult
from myapp.scraper import google

app = Flask(__name__)
flask_app = app

admin = admin.Admin(app, 'Hobby Project')
admin.add_view(ModelView(WebResult))
# flask_app.config.from_pyfile('config.cfg')

app.debug = True

app.config['MONGODB_DB'] = 'test'
app.config['MONGODB_HOST'] = 'mongodb://127.0.0.1:27017/'
# app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_USERNAME'] = 'hello'
app.config['MONGODB_PASSWORD'] = 'world'


db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)

google_search = google.GoogleSearch()

@app.route('/', methods=['GET'])
def index():
    res = WebResult.objects()
    # ross.search_str = 'dummy'
    # ross.save()
    return render_template('index.html', results=res)

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/search', methods=['POST'])
def search():
    search_str = request.form['search']

    existing_result = WebResult.objects(search_str=search_str)

    if existing_result is None or len(existing_result) == 0:
        results = google_search.getResult(search_str)

        record = WebResult()
        record.search_str = search_str
        record.data = results
        record.save()
    else:
        results = existing_result[0].data

    return render_template('search.html', title=search_str, results=results)

@app.route('/search/<search_str>', methods=['GET', 'POST'])
def search_web(search_str):
    
    existing_result = WebResult.objects(search_str=search_str)

    if existing_result is None or len(existing_result) == 0:
        results = {}
    else:
        results = existing_result[0].data

    return render_template('search.html', title=search_str, results=results)


@app.route('/delete/<search_str>', methods=['GET'])
def delete_res(search_str):

    existing_result = WebResult.objects(search_str=search_str)
    for res in existing_result:
        res.delete()

    return redirect('/', code=302)

# Result list page
# Single Result Page : search query, result page


# Google
# Wikipedia
# Twitter
# FB
# LinkedIn
#
