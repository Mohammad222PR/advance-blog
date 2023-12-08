from django import forms
from .models import *


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["author", "status"]
