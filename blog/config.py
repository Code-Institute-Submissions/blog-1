import os

# Application configurations.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        "db": "blog",
        "host": "mongodb://localhost/blog"
    }