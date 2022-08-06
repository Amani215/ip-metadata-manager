from functools import wraps
from http.client import UNAUTHORIZED
from flask import Blueprint
from flask import Blueprint, jsonify, request
from model.user import User
import service.auth as auth_service

auth_api = Blueprint('auth_api', __name__)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            if ('Authorization' not in request.headers) or (not request.headers['Authorization']):
                raise Exception("A valid token is missing")

            token = request.headers['Authorization']

            current_user = auth_service.get_authorized_user(token)
        except Exception as e:
            return jsonify({'message': str(e)}), UNAUTHORIZED

        return f(current_user, *args, **kwargs)
    return decorator


@auth_api.route('/api/auth/', methods=['POST'])
def authenticate():
    username = request.json['username']
    password = request.json['password']
    return auth_service.authenticate_user(username=username, password=password)


@auth_api.route('/api/auth/', methods=['GET'])
@token_required
def get_authorized_user(user: User):
    return jsonify(user.serialize)
