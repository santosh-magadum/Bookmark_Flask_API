from sqlalchemy import create_engine
from sqlalchemy import orm
import os
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")

 #'mysql://root:santosh&123@localhost/fastapi'


engine=create_engine(
    SQLALCHEMY_DATABASE_URL
 )


SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)


Base=declarative_base()

def get_db():
     db=SessionLocal()
     try:
         yield db
     finally:
         db.close()

