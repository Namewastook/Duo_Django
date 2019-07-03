from django.urls import path
from . import views

from .views import add_profile, update_profile

urlpatterns = [
    path('', views.index, name='Profile'),
    path("add/", add_profile, name="add"),
    path("update/<int:id>", update_profile, name="update")
]