from django.urls import path
from . import views

urlpatterns = [
    path('/Pantry', views.index, name='Pantry'),
]
