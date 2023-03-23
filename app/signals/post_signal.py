from app.models import Post
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
import random

def slugify_instance_title(instance, save=False, new_slug=None):
    print('icicicicicicicic')
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    qs = Post.objects.filter(slug=slug).exclude(id=instance.id)

    if qs.exists():
        rand_int = random.randint(100_000, 900_0000)
        slug = f'{slug}-{rand_int}'
        return slugify_instance_title(instance, save, slug)

    instance.slug = slug
    if save:
        instance.save()
    return instance


def post_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance)


def post_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, True)


post_save.connect(post_post_save, sender=Post)
pre_save.connect(post_pre_save, sender=Post)
