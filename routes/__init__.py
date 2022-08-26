from app import app
from .user import user_bp
from .auth import auth_bp

app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
