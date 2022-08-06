from functools import wraps
from http.client import UNAUTHORIZED
from flask import jsonify, request
import service.auth as auth_service

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