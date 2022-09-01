from flask import Blueprint, request
from model.user import User, users_schema, user_schema
from model import db
from flask_jwt_extended import jwt_required

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 1, type=int)
    data = User.query.paginate(page=page, per_page=per_page)
    return dict(items=users_schema.dump(data.items), total=data.total, current_page=data.page, per_page=data.per_page)    

@user_bp.route('/', methods=['POST'])
@jwt_required()
def post_user():
    content = request.json
    user = User(username=content['username'], password=content['password'])
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)