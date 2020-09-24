from django.urls import path
from . import views
from django.contrib.auth.models import User
from django.contrib import auth

urlpatterns = [
     path('myprofile/', views.myprofile, name='myprofile'),
     path('mylist/', views.mylist, name='mylist'),
     path('result/', views.SearchFormView, name='result'),
     
]