from bcrypt import checkpw, gensalt, hashpw
from flask import make_response
from model.user import User
from app import db
from sqlalchemy.exc import SQLAlchemyError

def create_user(username, password):
    password = hashpw(password.encode('utf-8'), gensalt())
    password = password.decode('utf8')
    user = User(username, password)

    try:
        db.session.add(user)
        db.session.commit()
        return {"user_id":user.id}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return {"error":error}

def get_users():
    return User.query.all()

def get_by_username(name:str)->User:
    user:User = User.query.filter_by(username=name).one()
    return user

def get_by_id(id)->User:
    return User.query.filter_by(id=id).one()

def verify_user(username, password):
    user: User = get_by_username(username)
    if checkpw(password.encode('utf-8'), user.password.encode('utf-8')) == True:
        return user
    else:
        return make_response('Could not verify',  401, {'Authentication': '"login required"'})