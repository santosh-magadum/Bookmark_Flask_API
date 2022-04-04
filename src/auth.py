from flask import Blueprint


auth=Blueprint("auth",__name__,url_prefix="/pi/v1/auth")


@auth.post('/register')
def register():
    return "User created"

@auth.get('/me')
def me():
    return {"User":"myself"}