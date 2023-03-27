from django.test import TestCase
from app.models  import Post, Tag, Category
from django.contrib.auth import get_user_model
from django_quill.quill import Quill
import  json

# Create your tests here.

User = get_user_model()
class PostTestCase(TestCase):
    def setUp(self):

        j = json.loads('{"delta":"{"ops":[{"insert":"test"}]}","html":"<p>test</p>"}')
        # val = Quill()
        self.user = User.objects.create_user('p@gmail.com', password='1234abcd')
        self.tag =Tag.objects.create(name='Guyane')
        self.category =Category.objects.create(name='Guyane')
        self.post = Post.objects.create(user=self.user, title='test', description='test', category=self.category, body=val )
        self.post.tag.add(self.tag)
        self.post.save()


    def test_post_user(self):
        self.assertEqual(self.post.user, self.user)