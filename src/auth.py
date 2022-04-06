from flask import Blueprint,request,jsonify
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST

from src import schemas

from flask_pydantic import validate

from pydantic import BaseModel

from src import models

from sqlalchemy.orm import Session

from sqlalchemy.sql.expression import select
from src import database


auth=Blueprint("auth",__name__,url_prefix="/pi/v1/auth")

class userCreate(BaseModel):
    email:str
    password:str
    username:str 


@auth.post('/register')
@validate(body=userCreate)
def register(db=next(database.get_db())):
    # try:
    # user=userCreate(**request.json)


    
    

    new_user=models.User(**request.json)
    # print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id":new_user.id,"username":new_user.username,"email":new_user.email}

    



    
    
    
    


    





    # except Exception as e:
        # print("error is",dir(e.json))
        # print("error is",e.json.__str__)
        # print(jsonify(e.errors()))
        # return jsonify(e.errors())
    # print(data)
    # user:userCreate=request.json
    # print("inside")
    # print("user",user)
    # print("request",request)

    # print(user.email)
    # print(user.password)
    # print(user.username)

    # username=request.json['username']
    # email=request.json['email']
    # password=request.json['password']
    # print(password)

    # return jsonify(user)
    # print(request)
    return jsonify({'error':'password is too short'})
    # ,HTTP_400_BAD_REQUEST



@auth.get('/me')
def me():
    return {"User":"myself"}