from django.urls import path
from . import views

urlpatterns = [
    path('/Profile', views.index, name='Profile'),
]
