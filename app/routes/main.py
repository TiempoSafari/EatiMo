from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.emotion import Emotion

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """首页路由"""
    return render_template('emotions.html', emotions=Emotion.query.all())

@main_bp.route('/profile')
@login_required
def profile():
    """用户个人中心"""
    return render_template('profile.html', user=current_user) 