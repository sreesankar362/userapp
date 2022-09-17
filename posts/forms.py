from django.forms import ModelForm
from django import forms
from posts.models import PostModel


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = [
            "post"
        ]
        widgets = {

            "post": forms.Textarea(attrs={"class":"form-control",'placeholder': 'Write Something..'}),
        }