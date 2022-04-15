

from flask import Flask,jsonify
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import engine
# from src.database import db
from src import models
# from flask_jwt_extended import JWTManager

def create_app(test_config=None):

    app=Flask(__name__,
    instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
                SECRETE_KEY=os.environ.get("SECRETE_KEY"),
                JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
                # SECRETE_KEY=os.environ.get("SECRET_KEY"),
        )

    else:
        app.config.from_mapping(test_config)


    # db.app=app

    models.Base.metadata.create_all(bind=engine)

    # JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    

    # @app.get("/")
    # def index():
    #     return "Hello world2"

    # @app.get("/hello")
    # def hello():
    #     return jsonify({"Hello":"World2"})

    return app