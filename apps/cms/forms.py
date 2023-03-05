from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length

class LoginForm(Form):
    email = StringField(validators=[InputRequired(message="Please enter your email"), Email(message='Invalid email')])
    password = StringField(validators=[Length(6, 20, message='Please enter password between 6 and 20 characters')])
    remember = IntegerField()