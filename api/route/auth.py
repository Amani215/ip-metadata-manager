from flask import Blueprint
from flask import Blueprint, jsonify, request
from model.user import User
import service.auth as auth_service
from middleware.token_required import token_required

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/api/auth/', methods=['POST'])
def authenticate():
    username = request.json['username']
    password = request.json['password']
    return auth_service.authenticate_user(username=username, password=password)

@auth_api.route('/api/auth/', methods=['GET'])
@token_required
def get_authorized_user(user: User):
    return jsonify(user.serialize)
