import articles
from django.db.models import query
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ArticleForm
from .models import Article
import requests

# News API -top head
API_KEY = '2d6d8492d8e540cc85c55714acbf6fcb'

# validate query parameters
def is_valid_queryparam(param):
    return param != '' and param is not None

# all news in french
def newsapi(request):
    # country = request.GET.get('country')
    country = 'fr'
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

def about_us(request):
    return render(request, 'articles/about_us.html', {})

# Retreve all and search by category
def index(request):
    articles = Article.objects.all()
    category = request.GET.get('category')
    if (is_valid_queryparam(category)):
        articles = Article.objects.all().filter(category__contains=category)
    else:
        articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})

# get one article
def single_article(request, slug):
    item = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/single_article.html', {'item': item})

# create new article
def create_article(request):
    return render(request, 'articles/create_article.html', {})

