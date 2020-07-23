from blog import db, login_manager
from flask_login import UserMixin

# Data model for creating a User object.
class User(UserMixin, db.Document):
    meta = {"collection": "users"}
    username = db.StringField(required=True, max_length=32)
    email = db.StringField(required=True)
    password = db.StringField(required=True, max_length=255)
    profile_pic = db.StringField(default="default.png")

# Load User to current session.
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()