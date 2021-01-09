from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegistrationForm(FlaskForm):
    name = StringField('Name')
    email = StringField('E-mail')
    submit = SubmitField('Register')
