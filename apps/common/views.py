from flask import Blueprint

bp = Blueprint('common', __name__, url_prefix='/common')


@bp.route('/')
def index():
    return 'common index'