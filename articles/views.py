from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView
from .forms import ArticleModelForm
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

# # about us
# class AboutusPageView(TemplateView):
#     template_name = "articles/about_us.html"

def about_us(request):
    return render(request, 'articles/about_us.html', {})

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
def single_article(request, slug):
    try:
        item = get_object_or_404(Article, slug=slug)
        return render(request, 'articles/single_article.html', {'item': item})
    except Exception:
        messages.add_message(request, messages.WARNING, "Ups...Un tel article n'existe pas")
        return redirect('/')

# update the article
class ArticleUpdateView(UpdateView):
    template_name = "articles/update_article.html"
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    def get_success_url(self):
        return reverse("articles:index")

# delete article
class ArticleDeleteView(DeleteView):
    template_name = "articles/delete_article.html"
    queryset = Article.objects.all() 

    def get_success_url(self):
        return reverse("articles:index")

# create new article
class ArticleCreateView(CreateView):
    template_name = "articles/create_article.html"
    form_class = ArticleModelForm

    def get_success_url(self):
        return reverse("articles:index")

