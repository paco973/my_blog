from django.urls import path

from dashboard.views.user_view import UserView
from dashboard.views.post_view import PostView
from dashboard.views.home_view import HomeView

urlpatterns = [
    path('profile/', UserView.as_view(), name='user'),
    path('dashboard/', HomeView.as_view(), name='dashboard'),
    path('dashboard/post/create/', PostView.as_view(), name='create_post'),
    path('dashboard/post/edit/<slug:slug>/', PostView.as_view(), name='edit_post')
]