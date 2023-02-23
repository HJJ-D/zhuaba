from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired

from app.validator.base import BaseForm


class CommodityForm(BaseForm):
    commodity_id = IntegerField(validators=[DataRequired(message='commodity_id cannot be empty')])
    commodity_name = StringField(validators=[DataRequired(message='commodity_name cannot be empty')])
    price = FloatField(validators=[DataRequired(message='price cannot be empty')])
    remaining_num = IntegerField(validators=[DataRequired(message='remaining_num cannot be empty')])
    image = StringField(validators=[DataRequired(message='image cannot be empty')])
