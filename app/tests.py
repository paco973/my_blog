from django.test import TestCase
from app.models  import Post, Tag, Category
# Create your tests here.
class PostTestCase:
    def setUp(self):
        tag =Tag.objects.create(name='Guyane')
        category =Category.objects.create(name='Guyane')
        Post.objects.create(title='test', description='test', tag=tag, category=category, body='test')

