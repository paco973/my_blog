from django.db import models

from app.models import Post
from user_profile.models import User


class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)