# this pg is for laying out form objects 
# that describe the fields of my forms
#types of data in my forms and any restrictions 
# or validations needed by my forms

#Now we need imports, this file needs to know what it Is communicating with
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField 
from wtforms.validators import DataRequired, Email, EqualTo

#fields available StringField, SubmitField, 
# PasswordField, decimal fields, integerfields, 
# phone number fields find in wtforms https://flask-wtf.readthedocs.io/en/1.0.x/



#flaskform is core class/object we are building
# off of, we are building form, they are going 
# to be children of the flask form. So there is 
# going to be a little bit of inheritence going on.
#Flask forms is a class which contains a whole 
# bunch of code making form data work the way we 
# want it to, we just provide slight modificaitons 
# to get forms the way we want it to.

#layout class, 1 for each form we are going to need

#if I want signup/in form my class to work off 
# flask form class, I need to tell them too, or 
# if I want signup/in class to inherit from flask 
# form tell them too

# this tells class signinform to inherit from flaskform

class signupForm(FlaskForm):
#having done the inheritence - what we put inside 
# this class is just the fields that we want on 
# our form
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField() #doesnt say anything just button

class signinForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

#Now theres a bunch of code belonging to flask 
# form class that will also be applied to sign in 
# form, this is how we get the funcitonality 
# without writting a bunch of code

class updateUsernameForm(FlaskForm):
    newusername = StringField('New Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Change Username')

    
