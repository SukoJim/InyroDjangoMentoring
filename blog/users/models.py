from django.db import models
from posts.models import Post
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    username = models.CharField(max_length= 20, unique=True)
    nickname = models.CharField(max_length=50, default = "Jim")


class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  

class Reply(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)  
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  

class Like(models.Model):
    LIKE_TYPES = (
        ('Post', 'Post'),
        ('Comment', 'Comment'),
        ('Reply', 'Reply'),
    )
    like_type = models.CharField(max_length=7, choices=LIKE_TYPES)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)  
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)  
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, null=True, blank=True)  

class Category(models.Model):
    category_name = models.CharField(max_length=30)
