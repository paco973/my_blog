from django.db import models


class PostView(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    key = models.TextField(null=True)
