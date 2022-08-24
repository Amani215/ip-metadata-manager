from flask_openapi3 import OpenAPI, Info

info = Info(title='IP metadata API', version='1.0.0')
app=OpenAPI(__name__, info = info)

import config

# Create tables
from model import db
from model.user import User
from model.ip_address import IPAddress

#Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# # close session at shutdown
# @app.teardown_appcontext
# def shutdown_session(exception=None):
#    db_session.remove()

# db.drop_all()
db.create_all()

#  routing
from route.user import user_api
from route.ip_address import ip_api
from route.auth import auth_api

app.register_api(user_api)
app.register_api(ip_api)
app.register_api(auth_api)

@app.route('/')
def home():
   return "<h1>hello world!</h1>"

if __name__ == '__main__':
    app.run()