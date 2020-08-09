from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

# Post creation form with data validation.
class CreateOrUpdatePostForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired(), Length(min=5, max=32)]
    )
    content = TextAreaField(
        "Your Post",
        validators=[DataRequired(), Length(min=5, max=255)]
    )
    submit = SubmitField("Post")