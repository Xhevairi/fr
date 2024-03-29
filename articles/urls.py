from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    )
from django.urls import path, reverse_lazy, reverse
from . import views

app_name = 'articles'

urlpatterns = [
    path('about_us/', views.AboutusPageView.as_view(), name='about_us'),
    # news in french language
    path('newsapi/', views.newsapi, name='newsapi'),
    path('articles/', views.articles, name='articles'),
    # articles
    path('', views.index, name='index'),
    path('single/<slug:slug>', views.ArticleDetailView.as_view(), name='single_article'),
    path('single/<slug:slug>/update', views.ArticleUpdateView.as_view(), name='update_article'),
    path('single/<slug:slug>/delete', views.ArticleDeleteView.as_view(), name='delete_article'),
    path('create/', views.ArticleCreateView.as_view(), name='create_article'),
    # register, login, logout and password reset 
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
