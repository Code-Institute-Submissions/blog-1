import os

# Application configurations.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
    'host': "mongodb+srv://Yaoma:pfc0a7aNQiF22Lek@cluster0-xbf5e.mongodb.net/blog?retryWrites=true&w=majority"
}