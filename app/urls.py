from .views.home_views import HommeView
from .views.post_view import PostView
from django.urls import path

urlpatterns = [
   path('', HommeView.as_view(), name='index'),
   path('post/', PostView.as_view(), name='post')
]
