from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField , FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from blog.models import User

# User login form with data validation.
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=32)]
    )
    submit = SubmitField("Login")

# User registration form data validation.
class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=5, max=32)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=32)]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords didn't match.")]
    )
    submit = SubmitField("Sign up")

    # Check if User with given Username already exists.
    def validate_username(self, username):
        existing_user = User.objects(username=username.data).first()
        if existing_user:
            raise ValidationError("This username is already taken. Please choose another one.")

    # Check if User with given Email already exists.
    def validate_email(self, email):
        existing_user = User.objects(email=email.data.lower()).first()
        if existing_user:
            raise ValidationError("This email is already taken. Please choose another one.")

# Update account info.
class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=5, max=32)]
    )
    profile_pic = FileField(validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField("Update")

    # Check if User with given Username already exists.
    def validate_username(self, username):
        if username.data != current_user.username:
            existing_user = User.objects(username=username.data).first()
            if existing_user:
                raise ValidationError("This username is already taken. Please choose another one.")