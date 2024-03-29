from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
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
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )
        field_classes = {
            'username': UsernameField,
            }
# create, update and delete if staff
class SignupAsStaff(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)