from flask import Blueprint, request
from model.user import User, users_schema, user_schema
from app import db
from flask_jwt_extended import jwt_required

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    data = User.query.all()
    return users_schema.dump(data)

@user_bp.route('/', methods=['POST'])
@jwt_required()
def post_user():
    content = request.json
    user = User(username=content['username'], password=content['password'])
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)