from django.db import models
from user_profile.models.user import User

class PostLike(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    key = models.ForeignKey(User, on_delete=models.CASCADE)
