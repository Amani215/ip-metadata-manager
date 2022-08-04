from flask import Blueprint
from flask import Blueprint, jsonify, request
import service.user as user_service

auth_api = Blueprint('auth_api',__name__)

@auth_api.route('/api/auth/', methods=['POST'])
def authenticate():
    username = request.form.get('username')
    password = request.form.get('password')
    result = user_service.verify_user(username=username, password=password)
    if(result == True):
        return "Authenticated :)"
    else:
        return "Not authenticated :(", 401