from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(3, 15, message='Between 3 to 15 characters')])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(5), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')
