from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired

from app.validator.base import BaseForm


class PurchaseHistoryForm(BaseForm):
    username = StringField(validators=[DataRequired(message='username cannot be empty')])
    date = DateTimeField(validators=[DataRequired(message='date cannot be empty')])
    commodity_id = IntegerField(validators=[DataRequired(message='commodity_id cannot be empty')])
    num = IntegerField(validators=[DataRequired(message='num cannot be empty')])