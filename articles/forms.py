from django import forms
from .models import Article

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