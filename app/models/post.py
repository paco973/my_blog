from django.contrib.auth import get_user_model
from django.db import models
from my_blog.middleware import get_current_user
from django.urls import reverse
from app.models.post_view import PostView
from .post_like import PostLike
from user_profile.models import User
from django_quill.fields import QuillField
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = QuillField()
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    tag = models.ManyToManyField('Tag')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'post/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def view(self) -> int:
        return len(PostView.objects.filter(post=self))

    def like(self) -> int:
        return len(PostLike.objects.filter(post=self))

    def save(self, *args, **kwargs):
        if not self.user:
            self.user = get_user_model().objects.get(pk=get_current_user().pk)

        super(Post, self).save(*args, **kwargs)

    def get_absolut_url(self):
        return reverse('post_detail', kwargs={"slug":self.slug})