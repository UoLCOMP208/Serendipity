from wtforms import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from ..forms import BaseForm
from wtforms import ValidationError
from utils import zlcache
from flask import g


class LoginForm(BaseForm):
    email = StringField(validators=[InputRequired(
        message="Please enter your email"), Email(message='Invalid email')])
    password = StringField(validators=[Length(
        6, 20, message='Please enter password between 6 and 20 characters')])
    remember = IntegerField()


class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(
        6, 20, message='Please enter correct format of old password')])
    newpwd = StringField(validators=[Length(
        6, 20, message='Please enter correct format of new password')])
    newpwd2 = StringField(validators=[EqualTo(
        "newpwd", message='Confirm password must be the same as new password')])


class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='Please enter correct format of email')])
    captcha = StringField(
        validators=[Length(min=6, max=6, message='Please enter correct format of captcha')])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_cache = zlcache.get(email)
        if not captcha_cache or captcha.lower() != captcha_cache.lower():
            raise ValidationError('Wrong captcha!')

    def validate_email(self, field):
        email = field.data
        user = g.cms_user
        if user.email == email:
            raise ValidationError('Please enter a new email!')

class AddBoardForm(BaseForm):
    name = StringField(validators=[InputRequired(message='Please enter board name!')])

class UpdateBoardForm(AddBoardForm):
    board_id = IntegerField(validators=[InputRequired(message='Please enter board id!')])