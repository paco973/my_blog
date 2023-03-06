from . import views
from django.urls import path

urlpatterns = [
   path('', views.HommeView.as_view())
]
