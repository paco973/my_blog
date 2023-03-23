from django.db import models
from user_profile.models.user import User

class PostView(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    key = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'post', 'key']

    def __str__(self):
        return f'{self.user}' 
