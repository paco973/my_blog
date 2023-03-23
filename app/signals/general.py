from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from app.models import Category, Tag
import random
def slugify_instance_name(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)

    if qs.exists():
        rand_int = random.randint(100_000, 900_0000)
        slug = f'{slug}-{rand_int}'
        return slugify_instance_name(instance, save, slug)

    instance.slug = slug
    if save:
        instance.save()
    return instance


def instance_with_slug_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_name(instance)


def instance_with_slug_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_name(instance, True)


post_save.connect(instance_with_slug_post_save, sender=Category)
pre_save.connect(instance_with_slug_pre_save, sender=Category)
post_save.connect(instance_with_slug_post_save, sender=Tag)
pre_save.connect(instance_with_slug_pre_save, sender=Tag)