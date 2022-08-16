from flask import jsonify, request
from model.user import User
import service.auth as auth_service
from middleware.token_required import token_required
from flask_openapi3 import APIBlueprint, Tag
from app import app

# auth_api = Blueprint('auth_api', __name__)
auth_api = APIBlueprint('auth_api',__name__)

auth_tag = Tag(name="auth", description="Authentication and Authorization requests")

@auth_api.route('/api/auth/', methods=['POST'])
@app.post('/api/auth', tags=[auth_tag])
def authenticate():
    """Authenticate the user
    
    Returns a json web token if the user is authenticated successfully
    """

    username = request.json['username']
    password = request.json['password']
    return auth_service.authenticate_user(username=username, password=password)

@auth_api.route('/api/auth/', methods=['GET'])
@app.get('/api/auth', tags=[auth_tag])
@token_required
def get_authorized_user(user: User):
    """Get the current authenticated user
    
    Returns the user object without the pasword according to the JWT
    """

    return jsonify(user.serialize)
