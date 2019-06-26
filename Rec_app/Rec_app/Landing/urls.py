from django.urls import path
from . import views

urlpatterns = [
    path('/Landing', views.index, name='Landing'),
]
