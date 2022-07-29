import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

_DB_URI = os.environ.get('DB_URL')
engine = create_engine(_DB_URI)

Base = declarative_base()