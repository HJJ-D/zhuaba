from wtforms import StringField, IntegerField, DateTimeField, FieldList
from wtforms.validators import DataRequired

from app.validator.base import BaseForm


class PurchaseHistoryForm(BaseForm):
    content = FieldList(StringField(validators=[DataRequired(message='Content cannot be empty')]))
    ## time = DateTimeField(validators=[DataRequired(message='date cannot be empty')])
    username = StringField(validators=[DataRequired(message='username cannot be empty')])
    car = StringField(validators=[DataRequired(message='car_id cannot be empty')])