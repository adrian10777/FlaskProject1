#1st line inside __init__.py file is we are going to need access to the pieces of functionality we are going to be using
#import our necessary modules/files/classes/packages/whatever else we need for this file to work
from flask import Flask
from config import Config
#notice it flags the flask= get flask package

#define our application as an instance of the flask object... aka tell computer this is a flask object
app = Flask(__name__) # tells flask that this is a flask app and this is called app

# tell our application to configure itself based on the config class
app.config.from_object(Config)

#tell our app where it can find its routing info
#note this import specifically (and later a models import) must ome AFTER the app is defined
from . import routes #routes has no light but being used
