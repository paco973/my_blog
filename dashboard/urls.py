from django.urls import path

from dashboard.views.user_view import UserView

urlpatterns = [
    path('dashboard/', UserView.as_view(), name='user')
]