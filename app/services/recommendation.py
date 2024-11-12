from app.models.recipe import Recipe, Tag
from app.models.emotion import Emotion
from sqlalchemy import or_

class RecommendationService:
    @staticmethod
    def get_recommendations(emotion_id, user_id=None, limit=5):
        """
        基于用户情绪推荐食谱
        
        Args:
            emotion_id: 情绪ID
            user_id: 用户ID（可选）
            limit: 返回推荐数量
            
        Returns:
            推荐的食谱列表
        """
        # 获取与情绪相关的食谱标签
        emotion = Emotion.query.get(emotion_id)
        if not emotion:
            return []
            
        # 获取情绪相关的标签
        related_tags = emotion.related_tags
        
        # 基础推荐逻辑
        recipes = Recipe.query.join(Recipe.tags).filter(
            Tag.name.in_(related_tags)
        ).distinct().limit(limit).all()
        
        # 如果没有找到足够的食谱，返回一些默认推荐
        if len(recipes) < limit:
            default_recipes = Recipe.query.filter(
                ~Recipe.id.in_([r.id for r in recipes])
            ).limit(limit - len(recipes)).all()
            recipes.extend(default_recipes)
        
        return recipes 