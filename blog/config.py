import os

# Application configurations.
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGODB_HOST = os.environ.get("MONGODB_HOST")