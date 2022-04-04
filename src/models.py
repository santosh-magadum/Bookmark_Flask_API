

from src.database import Base


from sqlalchemy import Column,String,Integer,Boolean,DateTime,ForeignKey

from sqlalchemy.sql.functions import now
from sqlalchemy.sql.expression import null,text

from sqlalchemy.orm import relationship

from sqlalchemy.orm import validates

import string

import random



class User(Base):

    __tablename__="users"


    id =Column(Integer,primary_key=True)
    username=Column(String(80),unique=True,nullable=False)
    email=Column(String(120),unique=True,nullable=False)
    password= Column(String(500),nullable=False)
    created_at=Column(DateTime(timezone=True),nullable=False,server_default=text('now()'))
    updated_at=Column(DateTime(timezone=True),nullable=False,onupdate=text('now()'))

    bookmarks=relationship("bookmarks",backref="users")



    def __repr__(self):
        return "User >>> {self.username}"


    @validates('email')
    def validate_email(self,key,value):
        if '@' not in value:
            raise ValueError("failed simple email validator")
        return value


class Bookmark(Base):

    __tablename__="bookmarks"

    id =Column(Integer,primary_key=True)
    body=Column(String(100),nullable=True)
    url = Column(String(200),nullable=False)
    short_url=Column(String(3),nullable=True)

    visits=Column(Integer,default=0)

    user_id=Column(Integer,ForeignKey("users.id"))

    created_at=Column(DateTime(timezone=True),nullable=False,server_default=text('now()'))
    updated_at=Column(DateTime(timezone=True),nullable=False,onupdate=text('now()'))
    

    def __repr__(self):
        return "Bookmark >>> {self.url}"


    def generate_short_characters(self):
        characters=string.digits+string.ascii_letters

        picked_chars=''.join(random.choices(characters,k=3))
        link =self.query.filter_by(short_url=picked_chars).first()

        if link:
            self.generate_short_characters()
        else:
            return picked_chars

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.short_url=self.generate_short_characters()

