import datetime
from flask import jsonify
import jwt
from model.user import User
from service.user import verify_user
from app import app

def authenticate_user(username, password):
    result = verify_user(username, password)

    if isinstance(result, User):
        token = jwt.encode({'public_id' : str(result.id), 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, app.config['SECRET_KEY'], "HS256")
        return jsonify({'token' : token})
    else:
        return result