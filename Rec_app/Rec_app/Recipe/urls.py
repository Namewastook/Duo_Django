from django.urls import path
from . import views

urlpatterns = [
    path('/Recipe', views.index, name='Recipe'),
]
