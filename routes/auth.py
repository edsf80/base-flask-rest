from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_expects_json import expects_json
from model.user import User

schema = {
  "type": "object",
  "properties": {
    "username": { "type": "string" },
    "password": { "type": "string" }
  },
  "required": ["username", "password"]
}

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
@expects_json(schema)
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username = username).first()
    if not user or user.password != password:
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(token=access_token)