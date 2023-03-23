from django.db import models
from django.shortcuts import reverse
from .post import Post


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/', default='paco.pgn', null=True)
    color = models.CharField(max_length=50, default=None, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def posts(self):
        return Post.objects.filter(category=self)

    def get_absolut_url(self):
        return reverse('category', kwargs={"slug":self.slug})