#we are going to set up the application's configuration using a class and some variables
#we are also going to help out the application by telling it a bit about it own file structure

#import - we need a bit of help from the os package

import os

#set base directory of the entire project - sothat our computer knows the location of various files in this project
#needs to be called basedir or else it wont work
basedir = os.path.abspath(os.path.dirname(__name__)) # this is telling our computer where is location of root folder basic flask set up, so when we tell a file were to find a route it is easier to reference to instead of dealing with cd to this folder and this folder etc

#next set up our configuration = how something is setup
class Config():
    """
    set config variables for our flask app
    """
#these 3 are specifically named like this
FLASK_APP = os.environ.get('FlASK_APP')
FLASK_ENV = os.environ.get('FLASK_ENV') # is this an app being developed currently or a production app that is publicly hosted
# flask has to less work in terms were it will skip security steps in production environment
SECRET_KEY = os.environ.get('SECRET_KEY')
#these are the three config variables we are going to need

#we want secret_key hidden, common practice to hide all config variables
#to do this we use .env file