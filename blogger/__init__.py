from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blogger.config import Config

app = Flask(__name__)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from blogger.users import bp as users_bp
    app.register_blueprint(users_bp)

    from blogger.posts import bp as posts_bp
    app.register_blueprint(posts_bp)

    from blogger.main import bp as main_bp
    app.register_blueprint(main_bp)

    from blogger.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app
