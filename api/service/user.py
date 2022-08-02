from bcrypt import checkpw, gensalt, hashpw
from model.user import User
from app import db
from sqlalchemy.exc import SQLAlchemyError

def create_user(username, password):
    password = hashpw(password.encode('utf-8'), gensalt())
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

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def verify_user(username, password):
    user = get_user_by_username(username)
    return checkpw(password, user.password)
