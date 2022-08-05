from functools import wraps
from flask import Blueprint
from flask import Blueprint, jsonify, request
import jwt
from model.user import User
import service.user as user_service
from app import app

auth_api = Blueprint('auth_api',__name__)

  
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

      token = None

      if 'x-access-tokens' in request.headers:
          token = request.headers['x-access-tokens']

      if not token:
          return jsonify({'message': 'a valid token is missing'})

      try:
          data = jwt.decode(token, app.config['SECRET_KEY'])
          current_user = User.query.filter_by(public_id=data['public_id']).first()
      except:
          return jsonify({'message': 'token is invalid'})

      return f(current_user, *args, **kwargs)
    return decorator

@auth_api.route('/api/auth/', methods=['POST'])
def authenticate():
    auth_data = request.authorization
    
    result = user_service.verify_user(username=auth_data.username, password=auth_data.password)
    if(result == True):
        return "Authenticated :)"
    else:
        return "Not authenticated :(", 401