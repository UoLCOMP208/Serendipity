from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from ..forms import BaseForm


class LoginForm(BaseForm):
    email = StringField(validators=[InputRequired(message="Please enter your email"), Email(message='Invalid email')])
    password = StringField(validators=[Length(6, 20, message='Please enter password between 6 and 20 characters')])
    remember = IntegerField()

class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6,20,message='Please enter correct format of old password')])
    newpwd = StringField(validators=[Length(6,20,message='Please enter correct format of new password')])
    newpwd2 = StringField(validators=[EqualTo("newpwd",message='Confirm password must be the same as new password')])