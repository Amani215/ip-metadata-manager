# import os
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base

# _DB_URI = os.environ.get('DB_URL')
# engine = create_engine('postgresql://db:pass@db:5432/db')

# Base = declarative_base()\

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://db:pass@db:5432/db')

Base = declarative_base()