from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/', default='paco.pgn', null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
