from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('newsapi/', views.newsapi, name='newsapi'),
    path('', views.index, name='index'),
    path('single_article/<slug:slug>', views.single_article, name='single_article'),
    path('create_article/', views.create_article, name='create_article'),
]