from wtforms import Form, StringField, SubmitField, DateTimeField
from wtforms.fields import FileField

from wtforms.widgets.html5 import DateTimeInput


class FileForm(Form):
    # life_time = DateTimeField('life_time', widget=DateTimeInput())
    life_time = StringField('life_time')
    file = FileField('file')
    submit = SubmitField()
