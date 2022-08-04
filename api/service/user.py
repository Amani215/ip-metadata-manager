from bcrypt import checkpw, gensalt, hashpw
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

def get_by_username(name):
    user:User = User.query.filter_by(username=name).one()
    userObj = {
            "id":user.id,
            "username":user.username,
            "password":user.password 
            }
    return user

def verify_user(username, password):
    user: User = get_by_username(username)
    return checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
