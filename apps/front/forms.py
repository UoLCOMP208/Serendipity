import wtforms
from ..forms import BaseForm
from wtforms.validators import Length, InputRequired
from wtforms import ValidationError
from utils import zlcache

# Form：Used to verify that the data submitted by the front-end meets the requirements


class SignupForm(BaseForm):
    # ensure that emamil is a valid email address and is end with @liverpool.ac.uk
    # email = wtforms.StringField('Email', validators=[Email(message="Invalid email address"),
    #     wtforms.validators.Regexp(".*@liverpool.ac.uk$", message="Email must be from liverpool.ac.uk domain")])
    email = wtforms.StringField(validators=
                                [wtforms.validators.Regexp('.*@liverpool.ac.uk$', message='Email must be from liverpool.ac.uk domain')])
    # captcha = wtforms.StringField(validators=[Regexp(r"\w{6}", message="Incorrect captcha format!")])
    username = wtforms.StringField(
        validators=[Length(min=3, max=20, message="Incorrect username format!")])
    password = wtforms.StringField(
        validators=[Length(min=6, max=20, message="Incorrect password format!")])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_cache = zlcache.get(email)
        
        if not captcha_cache or captcha.lower() != captcha_cache.lower():
            raise ValidationError(message='Wrong captcha!')
        
class SigninForm(BaseForm):
    email = wtforms.StringField(validators=
                                [wtforms.validators.Regexp('.*@liverpool.ac.uk$', message='Email must be from liverpool.ac.uk domain')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Incorrect password format!")])
    remember = wtforms.StringField()

class AddPostForm(BaseForm):
    title = wtforms.StringField(validators=[InputRequired(message='Please enter title!')])
    content = wtforms.StringField(validators=[InputRequired(message='Please enter content!')])
    board_id = wtforms.IntegerField(validators=[InputRequired(message='Please enter board id!')])

class AddCommentForm(BaseForm):
    content = wtforms.StringField(validators=[InputRequired(message='Please enter content!')])
    post_id = wtforms.IntegerField(validators=[InputRequired(message='Please enter post id!')])