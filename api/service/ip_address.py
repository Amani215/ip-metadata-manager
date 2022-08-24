from model.ip_address import IPAddress
from app import db
from sqlalchemy.exc import SQLAlchemyError

def create_address(address:str, username:str):
    ip = IPAddress(address=address, username=username)

    try:
        db.session.add(ip)
        db.session.commit()
        return {"ip_id":ip.id}
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return {"error":error}

def get_addresses():
    return IPAddress.query.all()

def get_by_address(address:str)->IPAddress:
    ip:IPAddress = IPAddress.query.filter_by(address=address).one()
    return ip

def get_by_username(username:str)->IPAddress:
    ip:IPAddress = IPAddress.query.filter_by(username=username).one()
    return ip

def get_by_id(id)->IPAddress:
    return IPAddress.query.filter_by(id=id).one()