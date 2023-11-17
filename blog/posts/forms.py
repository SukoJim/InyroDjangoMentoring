from django import forms
from markdownx.fields import MarkdownxFormField
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']
        widgets = {'content': forms.Textarea(attrs={'rows': 5})}