from flask import Blueprint, render_template
from blog.users.forms import LoginForm

users = Blueprint("users", __name__)

@users.route("/login")
def login():
    form = LoginForm()
    return render_template("users/login.html", form=form)