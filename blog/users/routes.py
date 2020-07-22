from flask import Blueprint, render_template, flash, redirect, url_for
from blog import bcrypt
from blog.users.forms import LoginForm, RegisterForm
from blog.models import User

# Exporting user routes.
users = Blueprint("users", __name__)

# User login route.
@users.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        pass
    return render_template("users/login.html", title="Login", form=login_form)

# User register route.
@users.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        # Hashing password for security reasons.
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode("utf-8")
        # Creating new User.
        new_user = User(
            username=register_form.username.data,
            email=register_form.email.data.lower(),
            password=hashed_password
        )
        # Saving User to database.
        new_user.save()
        flash("Account has been successfully created. You can now login.", "success")
        return redirect(url_for("users.login"))
    return render_template("users/register.html", title="Register", form=register_form)