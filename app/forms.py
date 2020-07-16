from wtforms import Form, StringField, SubmitField, DateTimeField, DecimalField
from wtforms.fields import FileField
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, NumberRange

from wtforms.widgets.html5 import DateTimeInput


class FileForm(FlaskForm):
    # life_time = DateTimeField('life_time', widget=DateTimeInput())
    life_time = DecimalField('life_time', validators=[
        DataRequired(), NumberRange(min=1, max=5, message='not in range')])
    file = FileField('file', validators=[DataRequired()])
    submit = SubmitField()
