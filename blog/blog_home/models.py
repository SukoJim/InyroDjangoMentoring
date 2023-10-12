from django.db import models
from django.utils import timezone
# Create your models here.
class UserProfile(models.Model):
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    email = models.EmailField()


class Post(models.Model):
    # 기존 필드들
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 새로운 필드들
    viewCount = models.PositiveIntegerField(default=0)

    createdTimastamp = models.DateTimeField(default=timezone.now)
    modifiedTimestamp = models.DateTimeField(auto_now=True)