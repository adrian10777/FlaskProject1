# import sqlalchemy to create our instance of our ORM (translator between python and SQL)
from flask_sqlalchemy import SQLAlchemy

#import our LoginManager and instantiate
from flask_login import LoginManager, UserMixin

# imports for tools for our models
from datetime import datetime, timezone #not flask package part of python
from werkzeug.security import generate_password_hash
from uuid import uuid4

# create the instance of SQLAlchemy obj
db = SQLAlchemy() #<- mediator btwn models(user bluepint/user obj) and backbone of our app init.py

#instance of login manager
login = LoginManager()

# necessary user_loader function that flask_login needs us to write in order to work
@login.user_loader #this funcion(.user_loader) is necessary everytime you are using flask loginmanager with a user class that u are storing in a sql db,
def load_user(user_id):
    return User.query.get(user_id)

# let's set up our user obj,
# class user is going ot inherit from the sqlalchemy model
class User(db.Model, UserMixin): #this user is going to correspond to a table in our sql db
    id = db.Column(db.String, primary_key=True)
    username= db.Column(db.String(15), nullable=False, unique=True)
    email= db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=True, default='')
    last_name = db.Column(db.String(100), nullable=True,default='')
    password = db.Column(db.String(150), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password) #salt and has this password
        self.id = str(uuid4()) # generate id in some manner