from app import db
from app import ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("users.get_users", values=dict(id="<id>")),
            "collection": ma.URLFor("users.get_users"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)