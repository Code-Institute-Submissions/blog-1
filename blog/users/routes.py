from flask import Blueprint, render_template
from blog.users.forms import LoginForm, RegisterForm

users = Blueprint("users", __name__)

@users.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        pass
    return render_template("users/login.html", title="Login", form=login_form)

@users.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        pass
    return render_template("users/register.html", title="Register", form=register_form)