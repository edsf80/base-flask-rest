from flask import Blueprint, request
from model.user import User, users_schema, user_schema
from model import db
from flask_jwt_extended import jwt_required
from flask_expects_json import expects_json

schema = {
  "type": "object",
  "properties": {
    "username": { "type": "string" },
    "password": { "type": "string" }
  },
  "required": ["username", "password"]
}

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
@expects_json(schema)
def post_user():    
    user = user_schema.load(request.json)
    print(type(user))
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)