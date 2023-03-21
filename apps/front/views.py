from flask import Blueprint, views, render_template

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return 'front index'

class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')
    
bp.add_url_rule('/signup/',view_func=SignupView.as_view('signup'))