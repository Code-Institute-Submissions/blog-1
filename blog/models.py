from blog import db

# Data model for creating a User object.
class User(db.Document):
    meta = {"collection": "users"}
    username = db.StringField(required=True, max_length=32)
    email = db.StringField(required=True)
    password = db.StringField(required=True, max_length=255)