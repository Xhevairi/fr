from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import fields
from .models import Article

User = get_user_model()

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'category',
            'title',
            'authors',
            'content',
            'authors_image',
            'content_image',
            'slug',
        )

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
