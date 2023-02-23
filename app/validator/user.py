from wtforms import StringField
from wtforms.validators import DataRequired

from app.validator.base import BaseForm


class UserForm(BaseForm):
    username = StringField(validators=[DataRequired(message='Username cannot be empty')])
