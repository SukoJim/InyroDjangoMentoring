from django.contrib import admin
from django.urls import path

from . import views as views

urlpatterns = [
    path('postDetail/<int:post_id>/', views.postDetail, name='postDetail'),
    path('createPost/', views.createPost, name='createPost'),
    path('editPost/<int:post_id>/', views.editPost, name='editPost'),
    path('deletePost/<int:post_id>/', views.deletePost, name='deletePost'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('<int:post_id>/add_reply/<int:comment_id>/', views.add_reply, name='add_reply'),
]
