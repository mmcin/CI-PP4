from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('not_authorised', views.NotAuthorised, name='not_authorised'),
]