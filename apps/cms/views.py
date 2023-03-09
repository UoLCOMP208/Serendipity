from flask import Blueprint, views, render_template, request, session, redirect, url_for, g
from .forms import LoginForm
from .models import CMSUser
from .decorators import login_required
import config

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')

@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')

class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # if set session.permanent = True, the session will be saved for 31 days
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='Wrong email or password')
        else:
            message = form.errors.popitem()[1][0]
            return self.get(message=message)



bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
