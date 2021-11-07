from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class Form(FlaskForm):
    github_token = StringField(label='GitHub Token:', validators=[Length(min=2, max=30), DataRequired()])
    github_login = StringField(label='GitHub Login:', validators=[Length(min=2, max=30), DataRequired()])
    submit = SubmitField(label='Search')
