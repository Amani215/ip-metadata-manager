from crypt import methods
from flask import Blueprint, jsonify, request
import service.user as user_service

crud = Blueprint('crud',__name__)

@crud.route('/users', methods = ['GET'])
def get_users() -> str:
    users = user_service.get_users()
    return jsonify([i.serialize for i in users])

@crud.route('/signup', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    user_response = user_service.create_user(username=username, password=password)
    if ("error" in user_response.keys()):
        return user_response, 409
    return user_response

@crud.route('/auth', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')
    result = user_service.verify_user(username=username, password=password)
    if(result == True):
        return "Authenticated :)"
    else:
        return "Not authenticated :(", 401