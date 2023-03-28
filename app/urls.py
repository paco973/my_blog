from .views.home_views import HommeView
from .views.post_view import PostView
from django.urls import path
from .views.category_view import CategoryView
from .views.comment_view import CommentView

urlpatterns = [
    path('padpazdkp', HommeView.as_view(), name='index'),
    path('', PostView.as_view(), name='post'),
    path('post/<slug:slug>/', PostView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('comment/<slug:slug>/', CommentView.as_view(), name='comment')
]
