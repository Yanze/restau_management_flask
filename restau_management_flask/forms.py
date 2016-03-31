from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange

class AddGroupForm(Form):
  customer_nb = IntegerField('Customer_nb',
                             validators=[DataRequired(),
                             NumberRange(min=1, max=100)])

class ReleaseGroupTable(Form):
  customer_id = IntegerField('Customer_id',
                             validators=[DataRequired()])

class OrderDishesForm(Form):
  dish_nb = IntegerField('dish_nb', validators=[DataRequired()])
  customer_id = IntegerField('Customer_id',
                             validators=[DataRequired()])




