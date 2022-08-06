from flask import jsonify
import jwt
from schema.token import TokenSchema
from model.user import User
from service.user import verify_user, get_by_id
from app import app


def authenticate_user(username, password):
    result = verify_user(username, password)

    if isinstance(result, User):
        token_schema = TokenSchema(str(result.id)).serialize
        token = jwt.encode(token_schema, app.config['SECRET_KEY'], "HS256")
        return jsonify({'token': token})
    else:
        return result


def get_authorized_user(bearer_token: str) -> User:
    [bearer, token] = bearer_token.split(" ")
    if (bearer.upper() != "BEARER"):
        raise Exception("Token is not Bearer token")

    token_dict: dict = jwt.decode(token, app.config['SECRET_KEY'], "HS256")
    token_schema: TokenSchema = TokenSchema().fromDict(token_dict)

    user_id = token_schema.public_id
    return get_by_id(user_id)