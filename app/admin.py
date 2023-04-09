from django.contrib import admin

from app.models import Post, Notification, Reaction, Category, PostView,Tag, Comment
from app.models.news_letter import NewsLetter

# Register your models here.


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Notification)
admin.site.register(PostView)
admin.site.register(Reaction)
admin.site.register(Comment)
admin.site.register(NewsLetter)