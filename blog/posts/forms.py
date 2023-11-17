from django import forms
from markdownx.fields import MarkdownxFormField
from .models import Post
from users.models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category_name']
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['category_name'].required = False

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }