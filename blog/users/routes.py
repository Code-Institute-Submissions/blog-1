from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from blog import bcrypt
from blog.users.forms import LoginForm, RegisterForm, UpdateAccountForm
from blog.users.utils import save_profile_pic
from blog.models import User

# Exporting user routes.
users = Blueprint("users", __name__)

# User login route.
@users.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # Login User if User exists in database and credentials are correct.
        user = User.objects(email=login_form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash("Login unsuccessful. Check email and password.", "danger")
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

# User logout route.
@users.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out successfully.", "success")
    return redirect(url_for("users.login"))

# User update route.
@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    update_form = UpdateAccountForm()
    if update_form.validate_on_submit():
        if update_form.profile_pic.data:
            profile_pic = save_profile_pic(update_form.profile_pic.data)
            current_user.profile_pic = profile_pic
        current_user.username = update_form.username.data
        current_user.save()
        return redirect(url_for("users.account"))
    elif request.method == "GET":
        update_form.username.data = current_user.username
    profile_pic = url_for("static", filename="profile_pics/" + current_user.profile_pic)
    return render_template("users/account.html", title="Account", profile_pic=profile_pic, form=update_form)