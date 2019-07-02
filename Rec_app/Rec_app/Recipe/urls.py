from django.urls import path
from . import views

urlpatterns = [
    # path('', views.tester, name='Recipe'),
    # path('', views.seeding_db, name='Recipe'),
    path('', views.testing, name='Recipe'),

]
