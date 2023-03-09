from .views.sign_in import SigninView
from .views.sign_up_view import SignupView
from django.urls import path

urlpatterns = [
   path('signin/', SigninView.as_view(), name='signin'),
   path('signup/', SignupView.as_view(), name='signup' )
]
