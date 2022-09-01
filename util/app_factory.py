from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@127.0.0.1:3306/room'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    jwt = JWTManager()
    from model import db, ma
    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)    

    from routes import user_bp, auth_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    #from handlers.handlers import *
    return app