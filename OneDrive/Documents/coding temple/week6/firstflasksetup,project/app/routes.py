# import our main app from init
from app import app #givingroutes file access to the flask application as a whole, this allows us to let us create a route
#as well as import something from flask later

# allow flask routes to load html pgs with render_template()
from flask import render_template
from flask_login import login_required
#creating a route starts with a decorator
@app.route('/') #('/') -> url endpoint (going to be my home)

#depending on what ur doing with this route, sending data to user, or receiving data to ser it may need diff method, so u may see in data decorator a  methods=['GET','POST','PUT']
#in our scenario we are only using 'GET' (sending user data), but that's is default so u do not need, but it looks like this @app.route('/', methods=['GET'])

def home(): #function definition, home pg
    return render_template('index.html')

# last thing we need to do: we created this route and told it about the application but we havent told our __init__ or we havent given it access to the routes

@app.route('/about')
def about():
    return render_template('about.html', classname='Foxes78')


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')