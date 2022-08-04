from flask import Blueprint
from flask import Blueprint, jsonify, request
import service.user as user_service

user_api = Blueprint('user_api',__name__)

@user_api.route('/api/user/', methods = ['GET'])
def get_users() -> str:
    users = user_service.get_users()
    return jsonify([i.serialize for i in users])

@user_api.route('/api/user/', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    user_response = user_service.create_user(username=username, password=password)
    if ("error" in user_response.keys()):
        return user_response, 409
    return user_response