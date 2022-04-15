from flask import Blueprint,request,jsonify
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST,HTTP_200_OK,HTTP_201_CREATED,HTTP_403_FORBIDDEN,HTTP_401_UNAUTHORIZED,HTTP_404_NOT_FOUND

# from src.constants import http_status_codes

from src import schemas
import os
from flask_pydantic import validate

from pydantic import BaseModel

from src import models

from sqlalchemy.orm import Session

from sqlalchemy.sql.expression import select
from src import database

from src import util 

from src.schemas import userCreate

from src.util import verify_password

# from flask_jwt_extended import create_access_token,create_refresh_token

from datetime import datetime,timedelta


from flask import make_response

# from jwt import JWT
from jose import jwt


auth=Blueprint("auth",__name__,url_prefix="/pi/v1/auth")

# jwt_instance=JWT

# class userCreate(BaseModel):
#     email:str
#     password:str
#     username:str 

@auth.post('/relogin')
def dlogin():
    auth=request.authorization
    print(auth)

    # return {'message':'in dlogin Method'}
    return make_response('could not verfiry',401,{'WWW-Authenticate':'Basic realm="Login Required"'})

    ## use the os.urandom or uuid.uuid4().hex to generate the secrete key


@auth.post('/login')
def login(db=next(database.get_db())):
    email= request.json.get('email','')
    password= request.json.get('password','')

    query=select(models.User).where(models.User.email==email)

    user=db.execute(query).scalars().first()
   

    if not user:
        return {'Message':'Not valid user'},HTTP_404_NOT_FOUND
    is_pass_correct= verify_password(password,user.password)

    if is_pass_correct:
        # refresh=create_refresh_token(identity=user.id,expires_delta=timedelta(minutes=4))
        # access =create_refresh_token(identity=user.id,expires_delta=timedelta(minutes=4))

        data={'id':user.id,'exp':datetime.utcnow()+timedelta(minutes=30)}
        token = jwt.encode(data,os.environ.get("SECRETE_KEY"),algorithm='HS256')

        return jsonify({
            'user':{
                # 'refresh':refresh,
                # 'access':access,
                'username':user.username,
                'email':user.email,
                'jwt_token':token
                # 'id':user.id
            }
        }),HTTP_200_OK
    return jsonify({
        'error':'Wrong credentials'
    }),HTTP_401_UNAUTHORIZED







@auth.post('/register')
@validate(body=userCreate)
def register(db=next(database.get_db())):
    # try:
    # user=userCreate(**request.json)
    print("Inside register")
    

    
    try:
        new_user=models.User(**request.json)
        new_user.password=util.hash_password(new_user.password)
        print(new_user.password)
    except Exception as e:
        print(e)
        return {'error':str(e)}

   

    query=select(models.User).where(models.User.username==new_user.username)
    check_user=db.execute(query).scalars().first()
    # print(check_user)
    if check_user is None:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"id":new_user.id,"username":new_user.username,"email":new_user.email},HTTP_201_CREATED
    else:
        return {'Response':'The user is already exists in DB'},HTTP_403_FORBIDDEN

    



    
    
    
    


    





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
    # return jsonify({'error':'password is too short'})
    # ,HTTP_400_BAD_REQUEST



@auth.get('/me')
def me():
    return {"User":"myself"}