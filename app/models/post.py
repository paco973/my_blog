from django.contrib.auth import get_user_model
from django.db import models
from my_blog.middleware import get_current_user
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from app.models.post_view import PostView
from .post_like import PostLike
from user_profile.models import User
from django.db.models import Q
from django.utils.text import gettext_lazy as _
from django.utils import timezone


class STATUS(models.TextChoices):
    PUBLISHED = 'published', _('Published')
    REMOVED = 'removed', _('removed')
    DRAFT = 'draft', _('Draft')


class PostQuerySet(models.QuerySet):

    def search(self, query=None):
        if query is None:
            return self.all()
        elif query == '':
            return self.none()

        lookup = Q(title__icontains=query)
        return self.filter(lookup)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self.db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

    def get_published_post(self, query=None):
        return self.get_queryset().search(query=query).filter(status=STATUS.PUBLISHED,published_date__lt=timezone.now())


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    tag = models.ManyToManyField('Tag')
    status = models.CharField(max_length=50, choices=STATUS.choices, default=STATUS.DRAFT)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    published_date = models.DateTimeField(null=True, blank=True)

    objects = PostManager()

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
        return reverse('post_detail', kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse('edit_post', kwargs={"slug": self.slug})

    def get_status_color(self):
        if self.status == STATUS.PUBLISHED:
            return 'success'
        if self.status == STATUS.DRAFT:
            return 'warning'
        if self.status == STATUS.REMOVED:
            return 'danger'


# en django comment rendre le textField de mon model avec des outils d'édition comme sur word