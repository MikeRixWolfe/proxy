from flask import Flask

app = Flask(__name__, static_url_path='/proxy/static')
app.config.from_pyfile('app.cfg')

from app import views
