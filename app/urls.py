from .views.home_views import HommeView
from django.urls import path

urlpatterns = [
   path('', HommeView.as_view())
]
