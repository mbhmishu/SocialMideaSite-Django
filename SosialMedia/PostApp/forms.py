from django import forms
from PostApp.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'img',]
