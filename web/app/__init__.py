import os
from flask import Flask
from werkzeug.debug import DebuggedApplication
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta

app = Flask(__name__, static_folder='static')

# this DEBUG config here will be overridden by FLASK_DEBUG shell environment
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'bde092f73cf49e79fdff64de554f26ac20b3bff790564d0d'
app.config['JSON_AS_ASCII'] = False
app.permanent_session_lifetime = timedelta(minutes=60) # session timeout

app.config['CLIENT_ID'] = os.getenv("CLIENT_ID", None)
app.config['CLIENT_SECERT'] = os.getenv("CLIENT_SECERT", None)
app.config['REDIRECT_URI']= os.getenv("REDIRECT_URI", None)
app.config['SCOPE']= os.getenv("SCOPE", None)
app.config['AUTH_URL']= os.getenv("AUTH_URL", None)
app.config['TOKEN_URL']= os.getenv("TOKEN_URL", None)
app.config['GET_USER']= os.getenv("GET_USER", None)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'oauth_login'
login_manager.init_app(app)

from app import views  # noqa
