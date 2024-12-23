from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField

class SimpleRouteForm(FlaskForm):
    user_input = IntegerField("Enter number")
    submit = SubmitField("Submit", name="simple_submit")

class OddRouteForm(FlaskForm):
    user_input = IntegerField("Enter number")
    submit = SubmitField("Submit", name="odd_submit")