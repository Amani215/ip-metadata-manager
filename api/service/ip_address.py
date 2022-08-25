from model.user import User
from model.ip_address import IPAddress
from app import db
from sqlalchemy.exc import SQLAlchemyError
import service.user as user_service

def create_address(address:str, username:str):
    user:User = user_service.get_by_username(username)
    ip = IPAddress(_address=address, _user=user)

    try:
        db.session.add(ip)
        db.session.commit()
        return {"ip_id":ip.id}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return {"error":error}

def get_addresses():
    ips = IPAddress.query.all()

    for ip in ips:
        user:User = user_service.get_by_id(ip.userID)
        ip.user = user
    
    return ips

def get_by_address(address:str)->IPAddress:
    ip:IPAddress = IPAddress.query.filter_by(address=address).one()
    return ip

def get_by_username(username:str)->IPAddress:
    ip:IPAddress = IPAddress.query.filter_by(username=username).one()
    return ip

def get_by_id(id)->IPAddress:
    return IPAddress.query.filter_by(id=id).one()