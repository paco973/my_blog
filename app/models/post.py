from  django.db import models

from app.models.category import Category
from app.models.tag import Tag
from user_profile.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='paco/paco')
    created_at = models.DateTimeField(auto_now_add=True)