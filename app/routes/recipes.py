from flask import Blueprint, render_template, request, jsonify
from app.models.recipe import Recipe
from app.services.recommendation import RecommendationService
from flask_login import current_user, login_required
from app import db

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route('/recipes')
def list_recipes():
    """展示推荐的食谱列表"""
    emotion_id = request.args.get('emotion_id', type=int)
    if not emotion_id:
        return render_template('recipes.html', recipes=[])
        
    recipes = RecommendationService.get_recommendations(
        emotion_id=emotion_id,
        user_id=current_user.id if current_user.is_authenticated else None
    )
    return render_template('recipes.html', recipes=recipes)

@recipes_bp.route('/recipes/<int:recipe_id>')
def detail(recipe_id):
    """食谱详情页"""
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe_detail.html', recipe=recipe)

@recipes_bp.route('/api/recipes/favorite', methods=['POST'])
@login_required
def toggle_favorite():
    """切换食谱收藏状态"""
    recipe_id = request.json.get('recipe_id')
    recipe = Recipe.query.get_or_404(recipe_id)
    
    if recipe in current_user.favorites:
        current_user.favorites.remove(recipe)
    else:
        current_user.favorites.append(recipe)
    
    db.session.commit()
    return jsonify({'status': 'success'}) 