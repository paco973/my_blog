from django.contrib import admin

from app.models import Post, Notification, Reaction
from app.models.category import Category
from app.models.comment import Comment
from app.models.tag import Tag

# Register your models here.


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Notification)
admin.site.register(Comment)
admin.site.register(Reaction)