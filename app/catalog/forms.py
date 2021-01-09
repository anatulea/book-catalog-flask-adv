from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    submit = SubmitField('Update')