from functools import wraps
from flask import Blueprint
from flask import Blueprint, jsonify, request
import jwt
from model.user import User
import service.auth as auth_service
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
    username = request.json['username']
    password = request.json['password']
    return auth_service.authenticate_user(username=username, password=password)

@auth_api.route('/api/auth/', methods=['GET'])
def get_authorized_user():
    token  = request.headers.get('Authorization',type=str)
    return auth_service.get_authorized_user(token)
