from flask import Blueprint, render_template, request, redirect, url_for, flash
# auth routes need to use forms, import those forms
from app.forms import signupForm, signinForm, updateUsernameForm

# imports for working with our user model and signing users up and logins
from app.models import db, User
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

#creating auth blueprint, (named auth,import name of place the app is defined, tells this blueprint where it can find its html templates )
auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = signinForm() #create an instance, used by both GET AND POST

    if request.method == 'POST':
        if form.validate_on_submit():
            print("This user is ready to be checked if they gave the right username and password")
            print(form.username.data, form.password.data)
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or check_password_hash(user.password, form.password.data):
                # username didnt exist or user gave us wrong pass
                flash('Username or password did not match. Try again', category='danger')
                return redirect(url_for('auth.signin'))
            # implied else -> user and pass given match user in db
            login_user(user)
            flash(f'Thanks for logging in, {user.username}', category='info')
            return redirect(url_for('auth.home'))
        else:
            #we have bad form submission
            flash("Bad form input, try again", category='warning')
            return redirect(url_for('auth.signin'))

    return render_template('signin.html', form=form) #<- instance of signin form) #if GET
    # this blueprint auth knows where to find this html file because we told it what its template_folder will be aka 'auth_templates'

@auth.route('/register', methods=['GET', 'POST'])
def signup():
    #plan to use the signupForm here
    form = signupForm() #should be an object instantiation of a signup form obj, when we instantiate and instance of an obj, that is a function call to name of the class, dont forget parenthesis!!! no () doesnt make it a function
   
   # 2 scenarios
        #GET= render the template for the user
        #POST = take in the submitted form infor and do something with it
#set up a conditional that runs if method is POST
    if request.method == 'POST': #if user submitted the form
        #user trying to send us form info
        #validate the form info
        if form.validate_on_submit(): #this returns true or false saying either form input (given by user) works or returns false if it doesnt
            # we have proper user info
            print('successful new user data received')
            new_user = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data)
            print(f'New user vreated = {new_user.__dict__}')
            #once new user is created try to upload that user to our db
            # 2 things can go wrong  - we said username and email must be unique, if either is not unique we get an error
            try:
                db.session.add(new_user)
                db.session.commit()
            
            except:
                flash('Username or email taken.',category='warning')
                return redirect(url_for('auth.signup'))
            login_user(new_user)
            print(current_user, current_user.__dict__)
            flash(f"Thanks for signing up: {new_user.first_name} {new_user.last_name}!",category='info')
            return redirect(url_for('home'))
        else:
            #we have bad form submission
            flash("Bad form input, try again", category='warning')
            return redirect(url_for('auth.signup'))
            
    return render_template('signup.html', form=form) # this return works for GET

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('auth.signin'))

# build a route for a user profile pg- where they can update their info if they wnat
@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = updateUsernameForm() # used by both GET and Post
    # if user submits form
    if request.method =='POST':
        #validate the form they submitted
        #check their pass
        if form.validate_on_submit() and check_password_hash(current_user.password, form.password.data):
            #chekc if requested username is available
            #querying our db to see if the user name exists or not
            if User.query.filter_by(username=form.newusername.data).first():
                flash('Username already take, Please try a different one', category='danger')
                return redirect(url_for('auth.profile'))
            else:
                #following 4 lines are what we do is what we do if new username is available
                current_user.username = form.newusername.data # change the current users username attributes
                db.session.commit() #update the db with that new change
                flash('Your username has been updated!', category='success')
                return redirect(url_for('auth.profile'))
        #try to update their user
        # if it doesnt work, reset their user and tell them
        #if it does work, tell them
        else:
            flash('Incorrect password- try again.', category='danger')
            return redirect(url_for('auth.profile'))

        return render_template('profile.html', form=form) # GET
