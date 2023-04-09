from flask import Blueprint, views, render_template, request, session, url_for, redirect, g, abort
from exts import mail, db
from flask_mail import Message
from utils import restful, zlcache, safeutils
from .forms import SignupForm, SigninForm, AddPostForm, AddCommentForm
from .models import FrontUser
from ..models import BoardModel, PostModel, CommentModel
from .decorators import login_required
from flask_paginate import Pagination, get_page_parameter
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

# @bp.route("/post_guide")
# def post_guide():
#     return render_template("front/front_postguide.html")


@bp.route("/post_list")
def post_list():
    boards = BoardModel.query.all()
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page-1)*config.PER_PAGE
    end = start + config.PER_PAGE
    posts = PostModel.query.slice(start, end)
    pagination = Pagination(page=page, total=PostModel.query.count(
    ), outer_window=0, inner_window=2, show_single_page=True, per_page=2)
    context = {
        'boards': boards,
        'posts': posts,
        'pagination': pagination,
    }
    print(context)
    return render_template("front/front_postlist.html", **context)


@bp.route('/apost/', methods=['GET', 'POST'])
@login_required
def apost():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        return render_template('front/front_apost.html', boards=boards)
    else:
        form = AddPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.params_error(message='No such board!')
            post = PostModel(title=title, content=content)
            post.board = board
            post.author = g.front_user
            db.session.add(post)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=form.get_error())


@bp.route('/p/<post_id>/')
def post_detail(post_id):
    post = PostModel.query.get(post_id)
    if not post:
        abort(404)
    return render_template('front/front_pdetail.html', post=post)


@bp.route('/acomment/', methods=['POST'])
@login_required
def add_comment():
    form = AddCommentForm(request.form)
    if form.validate():
        content = form.content.data
        post_id = form.post_id.data
        post = PostModel.query.get(post_id)
        if post:
            comment = CommentModel(content=content)
            comment.post = post
            comment.author = g.front_user
            db.session.add(comment)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error('No such post!')
    else:
        return restful.params_error(form.get_error())


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
            user = FrontUser(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return restful.success()
        else:
            print(form.get_error())
            return restful.params_error(message=form.get_error())


@bp.route('/email/')
def send_email():
    message = Message('Serendipity Forum Email Test', recipients=[
                      'sgxshi6@liverpool.ac.uk'], body='Hello World!')
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

    message = Message('Serendipity Forum Email Captcha', recipients=[
                      email], body='Your email captcha is: %s' % captcha)
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


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
bp.add_url_rule('/signin/', view_func=SigninView.as_view('signin'))
