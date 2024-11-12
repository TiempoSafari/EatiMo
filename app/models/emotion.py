from app import db
from datetime import datetime

class Emotion(db.Model):
    __tablename__ = 'emotions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))  # 情绪图标URL
    related_tags = db.Column(db.JSON)  # 与该情绪相关的食谱标签
    
    # 情绪记录关联
    records = db.relationship('EmotionRecord', backref='emotion', lazy='dynamic')

class EmotionRecord(db.Model):
    __tablename__ = 'emotion_records'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    emotion_id = db.Column(db.Integer, db.ForeignKey('emotions.id'), nullable=False)
    intensity = db.Column(db.Integer)  # 情绪强度（1-5）
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.Column(db.Text)  # 用户记录的备注