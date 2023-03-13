from django.urls import path

from dashboard.views.user_view import UserView
from dashboard.views.post_view import PostView

urlpatterns = [
    path('dashboard/', UserView.as_view(), name='user'),
    path('dashboard/post/', PostView.as_view(), name='dashboard_geston_post')
]