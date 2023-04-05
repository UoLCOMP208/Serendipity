from flask import Blueprint, views, render_template, request, session, url_for, redirect
from exts import mail, db
from flask_mail import Message
from utils import restful, zlcache, safeutils
from .forms import SignupForm, SigninForm
from .models import FrontUser
from ..models import BoardModel
import string
import random
import config

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return render_template('front/front_index.html')

@bp.route('/logout')
def logout():
    del session[config.FRONT_USER_ID]
    return redirect(url_for('front.signin'))

@bp.route("/user_guide")
def user_guide():
    return render_template("front/front_userguide.html")

@bp.route("/post_guide")
def post_guide():
    return render_template("front/front_postguide.html")

@bp.route("/post_list")
def post_list():
    boards = BoardModel.query.all()
    context = {
        'boards': boards
    }
    return render_template("front/front_postlist.html", **context)


class SignupView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signup.html', return_to=return_to)
        return render_template('front/front_signup.html')

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = FrontUser(email=email,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return restful.success()
        else:
            print(form.get_error())
            return restful.params_error(message=form.get_error())


@bp.route('/email/')
def send_email():
    message = Message('Serendipity Forum Email Test', recipients=['sgxshi6@liverpool.ac.uk'], body='Hello World!')
    mail.send(message)
    return 'success'
                                                                  

@bp.route('/email_captcha/')
def email_captcha():
    # /email_capthca/?email=xxx@qq.com
    email = request.args.get('email')
    if not email:
        return restful.params_error('Please enter email!')

    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x), range(0, 10)))
    captcha = "".join(random.sample(source, 6))

    message = Message('Serendipity Forum Email Captcha', recipients=[email], body='Your email captcha is: %s' % captcha)
    print("Your email captcha is: %s" % captcha)
    try:
        mail.send(message)
    except:
        return restful.server_error()
    zlcache.set(email, captcha)
    return restful.success()

class SigninView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signin.html', return_to=return_to)
        return render_template('front/front_signin.html')
    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.FRONT_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(message='Wrong email or password!')
        else:
            return restful.params_error(message=form.get_error())
    
bp.add_url_rule('/signup/',view_func=SignupView.as_view('signup'))
bp.add_url_rule('/signin/',view_func=SigninView.as_view('signin'))