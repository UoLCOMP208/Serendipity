from flask import Blueprint, views

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return 'front index'

