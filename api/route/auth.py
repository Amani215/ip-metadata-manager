from functools import wraps
from flask import Blueprint
from flask import Blueprint, jsonify, request
import jwt
from schema.token import TokenSchema
from model.user import User
import service.auth as auth_service
from app import app

auth_api = Blueprint('auth_api',__name__)

  
def token_required(f):
    # @wraps(f)
    def decorator():
      token = None

      if 'Authorization' in request.headers:
          token = request.headers['Authorization']

      if not token:
          return jsonify({'message': 'a valid token is missing'})

    #   try:
    #       current_user = auth_service.get_authorized_user(token)
    #   except:
    #       return jsonify({'message': 'token is invalid'})

      return f()
    return decorator

@auth_api.route('/api/auth/', methods=['POST'])
def authenticate():
    username = request.json['username']
    password = request.json['password']
    return auth_service.authenticate_user(username=username, password=password)

@auth_api.route('/api/auth/', methods=['GET'])
@token_required
def get_authorized_user():
    token:str  = request.headers.get('Authorization',type=str)
    return auth_service.get_authorized_user(token)
