from django.contrib import admin
from django.urls import path

from . import views as views

urlpatterns = [
    path('home/',views.blog_home, name ='home'),
    path('postDetail/',views.postDetail, name='postDetail')
]
