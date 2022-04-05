from email.policy import default
from .models import Coment, Post
from django import forms 


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('id', 'upvotes')

class ComentCreateForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('author', 'content', 'post')