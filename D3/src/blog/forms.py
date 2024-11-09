from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        label = {
            'title': 'Title',
            'body': 'Body',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Write your post Title', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write post Body', 'class': 'form-control'}),
        }