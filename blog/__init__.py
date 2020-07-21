from flask import Flask
from blog.config import Config

def create_app(config_class=Config):
    from blog.main.routes import main

    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main)

    return app
