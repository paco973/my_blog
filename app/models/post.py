from django.db import models
from .post_view import PostView
from app.models.category import Category
from app.models.tag import Tag
from user_profile.models import User
from my_blog.middleware import get_current_user
from django_quill.fields import QuillField


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = QuillField()
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_current_user(), null=True)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_current_user(), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def view(self) -> int:
        return len(PostView.objects.filter(post=self))
