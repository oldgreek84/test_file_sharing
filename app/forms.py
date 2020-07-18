from wtforms import (Form, StringField, SubmitField, DateTimeField,
                     DecimalField)
from wtforms.fields import FileField
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, NumberRange


class FileForm(FlaskForm):
    ''' class create form to send file '''

    days_count = DecimalField('life_time',
            description='Enter number of days must safe your file',
            validators=[DataRequired(),
                        NumberRange(min=1,
                                    max=5,
                                    message='value must be in 1 to 5')])
    file = FileField('file', validators=[DataRequired()])
    submit = SubmitField()
    
