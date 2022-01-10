#1st line inside __init__.py file is we are going to need access to the pieces of functionality we are going to be using
#import our necessary modules/files/classes/packages/whatever else we need for this file to work
from flask import Flask
from config import Config

#import our blueprint, before the instantiation of flask obj line
from .api.routes2 import api
from .auth.routes3 import auth

# imports for our db stuff
from .models import db, login
#flask migrate allows us to easily make changes to our db
from flask_migrate import Migrate

#notice it flags the flask= get flask package

#define our application as an instance of the flask object... aka tell computer this is a flask object
app = Flask(__name__) # tells flask that this is a flask app and this is called app

# tell our application to configure itself based on the config class
app.config.from_object(Config)


# register our blueprint - create that link of communication
app.register_blueprint(api)
app.register_blueprint(auth)


#set up our ORM and Migrate connections
db.init_app(app)
migrate = Migrate(app, db) # obj communicates btwn (app, db) = app & db

# config for our login manager
login.init_app(app)
login.login_view = 'auth.signin'
login.login_message = 'Please sign in to see this page.'
login.login_message_category = 'danger'

#tell our app where it can find its routing info
#note this import specifically (and later a models import) must ome AFTER the app is defined
from . import routes #routes has no light but being used

# give the app/flask object access to its daatabase models
from . import models