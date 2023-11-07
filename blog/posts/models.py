from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(null = True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(null=False, default = '0')
    image = models.ImageField(upload_to = 'uploads/',null=True)
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)  
    category_name = models.ForeignKey('users.Category', on_delete=models.CASCADE)
