from django.db import models
from posts import Post
# Create your models here.

class UserProfile(models.Model):
    name = models.CharField((""), max_length=50)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=30)
    nickname = models.CharField((""), max_length=50)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Reference to the user who posted the comment

class Reply(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)  # Reference to the comment to which this reply is made
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Reference to the user who posted the reply

class Like(models.Model):
    LIKE_TYPES = (
        ('Post', 'Post'),
        ('Comment', 'Comment'),
        ('Reply', 'Reply'),
    )
    like_type = models.CharField(max_length=7, choices=LIKE_TYPES)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)  # Reference to the post if like is on a post
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)  # Reference to the comment if like is on a comment
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, null=True, blank=True)  # Reference to the reply if like is on a reply

class Category(models.Model):
    category_name = models.CharField(max_length=30)
