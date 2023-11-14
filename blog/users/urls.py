from django.contrib import admin
from django.urls import path

from . import views as views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
]