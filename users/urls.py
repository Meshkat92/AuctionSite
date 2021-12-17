"""Defines URL patterns for users"""
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    #Home Page
    path('', views.home, name='home'),
    #Login Page
    path('login/', views.login, name = 'login'),
    #Registration Page
    path('register/', views.register, name='register'),
    ]
