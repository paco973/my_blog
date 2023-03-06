from  django.db import models

from app.models.category import Category
from app.models.tag import Tag
from app.models.test import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)