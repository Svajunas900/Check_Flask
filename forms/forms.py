from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, HiddenField

class SimpleRouteForm(FlaskForm):
    user_input = IntegerField("Enter number")
    submit = SubmitField("Submit")

class OddRouteForm(FlaskForm):
    user_input = IntegerField("Enter number")
    submit = SubmitField("Submit")