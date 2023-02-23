from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from app.validator.base import BaseForm


class DriverForm(BaseForm):
    license_plate = StringField(validators=[DataRequired(message='license_plate cannot be empty')])
    username = StringField(validators=[DataRequired(message='username cannot be empty')])
    password = PasswordField(validators=[DataRequired(message='password cannot be empty')])
    nickname = StringField(validators=[DataRequired(message='nickname cannot be empty')])
