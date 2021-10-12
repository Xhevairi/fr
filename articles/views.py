from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import ArticleModelForm, CustomCreationForm
from .models import Article
import requests
from newsapp import settings

# News API country and key
country = settings.COUNTRY
API_KEY = settings.API_KEY

# signup
class SignupView(CreateView):
    form_class = CustomCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse("articles:login")

# validate query parameters
def is_valid_queryparam(param):
    return param != '' and param is not None

# all news in french
def newsapi(request):
    category = request.GET.get('category')

    if category:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles
    }    
    return render(request, 'articles/newsapi.html', context)

# about us
class AboutusPageView(TemplateView):
    template_name = "articles/about_us.html"

# Retreve all and search by category
def index(request):
    articles = Article.objects.all()
    category = request.GET.get('category')
    if (is_valid_queryparam(category)):
        articles = articles.filter(category__contains=category)
    else:
        articles = articles
    return render(request, 'articles/index.html', {'articles': articles})

# get one article
class ArticleDetailView(DetailView):
    template_name = "articles/single_article.html"
    queryset = Article.objects.all()
    context_object_name = "item"
    
# update the article
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "articles/update_article.html"
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    def get_success_url(self):
        return reverse("articles:index")

# delete article
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "articles/delete_article.html"
    queryset = Article.objects.all() 

    def get_success_url(self):
        return reverse("articles:index")

# create new article
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article 
    form_class = ArticleModelForm
    template_name = "articles/create_article.html"

    def get_success_url(self):
        return reverse("articles:index")

