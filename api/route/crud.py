from flask import Blueprint, jsonify
from model.user import User

crud = Blueprint('crud',__name__)

@crud.route('/users', methods = ['GET'])
def get_user_by_name():
    result = User.query.all()
    return jsonify([i.serialize for i in result])