from .views.home_views import HommeView
from .views.post_view import PostView
from django.urls import path
from .views.category_view import CategoryView


urlpatterns = [
   path('padpazdkp', HommeView.as_view(), name='index'),
   path('', PostView.as_view(), name='post'),
   path('post/<int:id>/', PostView.as_view(), name='post_detail'),
   path('category/<int:id>/', CategoryView.as_view(), name='category')
]
