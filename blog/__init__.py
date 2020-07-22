from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from blog.config import Config

db = MongoEngine()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    from blog.main.routes import main
    from blog.users.routes import users

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
