from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import TextAreaField, SubmitField

# Comment creation form with data validation.
class CommentForm(FlaskForm):
    content = TextAreaField(
        "Comment",
        validators=[DataRequired(), Length(min=5, max=255)]
    )
    submit = SubmitField("Comment")