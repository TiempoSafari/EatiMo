import os
import sys

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.emotion import Emotion
from app.models.recipe import Recipe, Tag

def init_db():
    app = create_app()
    
    # 确保instance目录存在
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    
    with app.app_context():
        # 创建所有表
        db.create_all()
        
        # 初始化标签
        tags_data = ['甜点', '小吃', '零食', '汤', '养生', '暖心', '辣', '重口味', '解压', '巧克力', 'comfort food']
        tags = {}
        for tag_name in tags_data:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.session.add(tag)
            tags[tag_name] = tag
        
        # 初始化一些示例食谱
        recipes_data = [
            {
                'name': '巧克力慕斯',
                'description': '香浓丝滑的巧克力慕斯，能让人心情愉悦',
                'ingredients': [
                    {'name': '黑巧克力', 'amount': '200g'},
                    {'name': '淡奶油', 'amount': '200ml'},
                    {'name': '糖', 'amount': '50g'},
                    {'name': '吉利丁片', 'amount': '3片'},
                    {'name': '鸡蛋', 'amount': '2个'},
                    {'name': '牛奶', 'amount': '100ml'}
                ],
                'steps': [
                    '1. 巧克力隔水融化',
                    '2. 吉利丁片泡软，加入温牛奶融化',
                    '3. 淡奶油打发至六分发',
                    '4. 将所有材料混合，倒入模具',
                    '5. 冷藏4小时以上'
                ],
                'cooking_time': 30,
                'difficulty': '中等',
                'calories': 350,
                'protein': 8.5,
                'carbs': 42.3,
                'fat': 18.7,
                'image_url': '/static/images/recipes/chocolate_mousse.jpg',
                'tags': ['甜点', '巧克力', 'comfort food']
            },
            {
                'name': '养生鸡汤',
                'description': '滋补养生的鸡汤，提供满满能量',
                'ingredients': [
                    {'name': '三黄鸡', 'amount': '1只'},
                    {'name': '枸杞', 'amount': '30g'},
                    {'name': '红枣', 'amount': '5颗'},
                    {'name': '姜片', 'amount': '3片'},
                    {'name': '盐', 'amount': '适量'},
                    {'name': '胡椒粉', 'amount': '少许'}
                ],
                'steps': [
                    '1. 鸡肉切块焯水',
                    '2. 锅中加水和所有材料',
                    '3. 大火煮沸后转小火炖煮1.5小时',
                    '4. 加入调味料即可'
                ],
                'cooking_time': 60,
                'difficulty': '简单',
                'calories': 200,
                'protein': 25.8,
                'carbs': 12.4,
                'fat': 8.2,
                'image_url': '/static/images/recipes/chicken_soup.jpg',
                'tags': ['汤', '养生', '暖心']
            },
            {
                'name': '麻辣火锅',
                'description': '热气腾腾的麻辣火锅，让人心情舒畅',
                'ingredients': [
                    {'name': '牛肉片', 'amount': '300g'},
                    {'name': '虾', 'amount': '200g'},
                    {'name': '金针菇', 'amount': '150g'},
                    {'name': '青菜', 'amount': '200g'},
                    {'name': '火锅底料', 'amount': '1包'},
                    {'name': '蒜末', 'amount': '2勺'},
                    {'name': '花生酱', 'amount': '2勺'},
                    {'name': '芝麻酱', 'amount': '2勺'}
                ],
                'steps': [
                    '1. 准备火锅底料和食材',
                    '2. 煮制汤底20分钟',
                    '3. 准备蘸料',
                    '4. 涮煮食材享用'
                ],
                'cooking_time': 90,
                'difficulty': '简单',
                'calories': 500,
                'protein': 35.6,
                'carbs': 28.9,
                'fat': 22.4,
                'image_url': '/static/images/recipes/hotpot.jpg',
                'tags': ['辣', '重口味', '解压']
            },
            {
                'name': '抹茶冰淇淋',
                'description': '清爽可口的抹茶冰淇淋，让心情平静下来',
                'ingredients': [
                    {'name': '抹茶粉', 'amount': '15g'},
                    {'name': '淡奶油', 'amount': '200ml'},
                    {'name': '糖', 'amount': '50g'},
                    {'name': '牛奶', 'amount': '100ml'},
                    {'name': '蛋黄', 'amount': '2个'}
                ],
                'steps': [
                    '1. 抹茶粉加热水调匀',
                    '2. 蛋黄打发加糖',
                    '3. 淡奶油打发',
                    '4. 混合所有材料',
                    '5. 倒入容器冷冻4小时'
                ],
                'cooking_time': 240,
                'difficulty': '中等',
                'calories': 280,
                'protein': 5.2,
                'carbs': 32.8,
                'fat': 15.6,
                'image_url': '/static/images/recipes/matcha_icecream.jpg',
                'tags': ['甜点', '小吃', '零食']
            },
            {
                'name': '暖心红豆汤',
                'description': '香甜可口的红豆汤，温暖身心',
                'ingredients': [
                    {'name': '红豆', 'amount': '200g'},
                    {'name': '糯米', 'amount': '50g'},
                    {'name': '红糖', 'amount': '80g'},
                    {'name': '桂圆', 'amount': '50g'},
                    {'name': '枸杞', 'amount': '20g'}
                ],
                'steps': [
                    '1. 红豆提前浸泡4小时',
                    '2. 锅中加水和红豆煮沸',
                    '3. 转小火熬煮1小时',
                    '4. 加入其他配料继续熬20分钟',
                    '5. 最后加入红糖调味'
                ],
                'cooking_time': 120,
                'difficulty': '简单',
                'calories': 180,
                'protein': 6.8,
                'carbs': 38.5,
                'fat': 2.4,
                'image_url': '/static/images/recipes/red_bean_soup.jpg',
                'tags': ['汤', '暖心', 'comfort food']
            }
        ]
        
        for recipe_data in recipes_data:
            if not Recipe.query.filter_by(name=recipe_data['name']).first():
                recipe = Recipe(
                    name=recipe_data['name'],
                    description=recipe_data['description'],
                    ingredients=recipe_data['ingredients'],
                    steps=recipe_data['steps'],
                    cooking_time=recipe_data['cooking_time'],
                    difficulty=recipe_data['difficulty'],
                    calories=recipe_data['calories'],
                    protein=recipe_data['protein'],
                    carbs=recipe_data['carbs'],
                    fat=recipe_data['fat'],
                    image_url=recipe_data['image_url']
                )
                # 添加标签
                for tag_name in recipe_data['tags']:
                    recipe.tags.append(tags[tag_name])
                db.session.add(recipe)
        
        # 初始化情绪数据
        emotions = [
            {
                'name': '开心',
                'description': '心情愉悦，想来点开心的美食',
                'icon': '😊',
                'related_tags': ['甜点', '小吃', '零食']
            },
            {
                'name': '疲惫',
                'description': '需要补充能量',
                'icon': '😪',
                'related_tags': ['汤', '养生', '暖心']
            },
            {
                'name': '焦虑',
                'description': '需要一些安抚的食物',
                'icon': '😰',
                'related_tags': ['甜品', '巧克力', 'comfort food']
            },
            {
                'name': '生气',
                'description': '来点美食消消气',
                'icon': '😠',
                'related_tags': ['辣', '重口味', '解压']
            },
            {
                'name': '伤心',
                'description': '需要一些温暖的食物',
                'icon': '😢',
                'related_tags': ['暖心', '甜品', 'comfort food']
            }
        ]
        
        for emotion_data in emotions:
            if not Emotion.query.filter_by(name=emotion_data['name']).first():
                emotion = Emotion(**emotion_data)
                db.session.add(emotion)
        
        try:
            db.session.commit()
            print("数据库初始化成功！")
        except Exception as e:
            print(f"初始化数据库时出错: {e}")
            db.session.rollback()

if __name__ == '__main__':
    init_db() 