from .views.sign_in import SigninView
from django.urls import path

urlpatterns = [
   path('signin/', SigninView.as_view(), name='signin')
]
