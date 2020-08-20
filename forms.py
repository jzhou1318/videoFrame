from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField


class SubmitForm(FlaskForm):
    inputFile = FileField()
    submit = SubmitField('Submit')
