from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blog.config import Config

db = MongoEngine()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    from blog.main.routes import main
    from blog.users.routes import users
    from blog.posts.routes import posts
    from blog.errors.handlers import errors

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
