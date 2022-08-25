from flask import jsonify, request
from model.user import User
from middleware.token_required import token_required
from app import app
import service.ip_address as ip_service
from flask_openapi3 import APIBlueprint, Tag

ip_api = APIBlueprint('ip_api',__name__)

ip_tag = Tag(name="IP", description="IP requests")

@ip_api.route('/api/ip/', methods = ['GET'])
@app.get('/api/ip', tags=[ip_tag])
@token_required
def get_addresses(user:User) -> str:

    """Get all ip addresses
    
    Returns all the ip addresses in the database
    """

    ips = ip_service.get_addresses()
    return jsonify([i.serialize for i in ips])


@ip_api.route('/api/ip/', methods=['POST'])
@app.post('/api/ip', tags=[ip_tag])
def add_address():
    """Add a new ip address
    
    Takes a username and an ip address and returns the new ip object ID.
    """

    address = request.form.get('address')
    username = request.form.get('username')

    user_response = ip_service.create_address(address=address, username=username)
    if ("error" in user_response.keys()):
        return user_response, 409
    return user_response