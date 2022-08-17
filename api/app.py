from flask_openapi3 import OpenAPI, Info

info = Info(title='IP metadata API', version='1.0.0')
app=OpenAPI(__name__, info = info)

import config

# Create tables
#from model import db

#####
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://db:pass@db:5432/db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

from model.user import User
#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
 ########
# db.drop_all()
#db.create_all()

#  routing
from route.user import user_api
from route.auth import auth_api

app.register_api(user_api)
app.register_api(auth_api)

@app.route('/')
def home():
   return "<h1>hello world!</h1>"

if __name__ == '__main__':
    app.run()