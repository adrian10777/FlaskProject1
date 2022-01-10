from flask import Blueprint

# actually set up our blueprint and enable communication btwn our blueprint and our main flask app

# computers are dumb - if we dont tell the blueprint to exist, it wont exist
#and if we dont tell the application how to talk to the blueprint we will have no idea how to talk to the blueprint

#Now we instantiate a blueprint
api = Blueprint('api', __name__, url_prefix='/api')
#blueprint(#name of blueprint, telling rest of application to refer this api as name of the variable called api, url_prefix -> for every route in this api do we want it to have a url prefix, yes! we want it to be apart of family of url's  )
#all we need to create a blueprint

# the decorator for a route belonging to a blueprint starts with @blueprint_name instead of @app

@api.route('/')
def test():
    return {'data': 'fancy data'}
    