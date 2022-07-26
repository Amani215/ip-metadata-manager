from flask import Blueprint

home_api = Blueprint('api',__name__)

@home_api.route('/api')
def welcome():
    # print('welcome')
    return '<h1>Welcome</h1>'