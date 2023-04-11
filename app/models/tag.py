from autoslug import AutoSlugField
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, populate_from='name')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    