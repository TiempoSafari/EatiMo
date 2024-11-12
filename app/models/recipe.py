from app import db
from datetime import datetime

# 食谱标签关联表
recipe_tags = db.Table('recipe_tags',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    ingredients = db.Column(db.JSON)  # 存储食材列表
    steps = db.Column(db.JSON)  # 存储制作步骤
    cooking_time = db.Column(db.Integer)  # 烹饪时间（分钟）
    difficulty = db.Column(db.String(20))  # 难度级别
    image_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 营养信息
    calories = db.Column(db.Float)
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)
    
    # 关联
    tags = db.relationship('Tag', secondary=recipe_tags, backref='recipes')
    ratings = db.relationship('Rating', backref='recipe', lazy='dynamic')

class Tag(db.Model):
    __tablename__ = 'tags'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)