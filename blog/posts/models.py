from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(null=False, default = '0')
    image = models.ImageField(upload_to = 'uploads/',null=True)
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)  
    category_name = models.ForeignKey('users.Category', on_delete=models.CASCADE, default = 0)

    def get_content_markdown(self):
        return markdown(self.content)


