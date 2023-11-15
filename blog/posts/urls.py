from django.contrib import admin
from django.urls import path

from . import views as views

urlpatterns = [
    path('postDetail/',views.postDetail, name='postDetail')
]
