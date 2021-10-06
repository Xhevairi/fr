from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('newsapi/', views.newsapi, name='newsapi'),
    path('', views.index, name='index'),
    path('single_article/<slug:slug>', views.single_article, name='single_article'),
    path('single_article/<slug:slug>/update', views.ArticleUpdateView.as_view(), name='update_article'),
    path('single_article/<slug:slug>/delete', views.ArticleDeleteView.as_view(), name='delete_article'),
    path('create_article/', views.ArticleCreateView.as_view(), name='create_article'),
]