from flask import jsonify, request

from model.user import User
from middleware.token_required import token_required
from app import app
import service.user as user_service
from flask_openapi3 import APIBlueprint, Tag

user_api = APIBlueprint('user_api',__name__)

user_tag = Tag(name="user", description="User requests")

@user_api.route('/api/user/', methods = ['GET'])
@app.get('/api/user', tags=[user_tag])
@token_required
def get_users(current_user:User) -> str:

    """Get all users
    
    Returns all the users in the database
    """

    users = user_service.get_users()
    return jsonify([i.serialize for i in users])


@user_api.route('/api/user/', methods=['POST'])
@app.post('/api/user', tags=[user_tag])
def add_user():
    """Add a new user
    
    Takes a username and a password and returns the new user ID. 
    If the username already exists the user is not added.
    """

    username = request.form.get('username')
    password = request.form.get('password')
    user_response = user_service.create_user(username=username, password=password)
    if ("error" in user_response.keys()):
        return user_response, 409
    return user_response