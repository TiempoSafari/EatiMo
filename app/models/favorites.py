from app import db
from datetime import datetime

# 用户收藏关联表
user_favorites = db.Table('user_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id')),
    db.Column('created_at', db.DateTime, default=datetime.utcnow)
) 