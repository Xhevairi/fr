from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from .forms import SignupAsStaff, ArticleModelForm, CustomCreationForm
from .models import Article
import requests
from newsapp import settings

# News API data
API_URL = settings.API_URL
country = settings.COUNTRY
API_KEY = settings.API_KEY

# validate query parameters
def is_valid_queryparam(param):
    return param != '' and param is not None

# all news in french
def newsapi_all(request):
    url = f'{API_URL}={country}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']    
    return articles
    
# news by category
def newsapi(request):
    category = request.GET.get('category')
    if category:
        url = f'{API_URL}={country}&category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        articles = newsapi_all(request)
    return render(request, 'articles/newsapi.html', {'articles': articles})

# all articles
def all_articles(request):
    articles = Article.objects.all()
    return articles

# news and articles
def index(request):
    # news api queryset
    news_api = newsapi_all(request)
    # articles queryset
    articles = all_articles(request)
    context = {
        'news_api': news_api,
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# articles by category
def articles(request):
    articles = all_articles(request)
    category = request.GET.get('category')
    if (is_valid_queryparam(category)):
        articles = articles.filter(category__contains=category)
    else:
        articles = articles
    return render(request, 'articles/articles.html', {'articles': articles})

# get one article
class ArticleDetailView(DetailView):
    template_name = "articles/single_article.html"
    queryset = Article.objects.all()
    context_object_name = "item"
    
# update the article
# class ArticleUpdateView(LoginRequiredMixin, UpdateView):
class ArticleUpdateView(SignupAsStaff, UpdateView):
    template_name = "articles/update_article.html"
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    def get_success_url(self):
        return reverse("articles:index")

# delete article
class ArticleDeleteView(SignupAsStaff, DeleteView):
    template_name = "articles/delete_article.html"
    queryset = Article.objects.all() 

    def get_success_url(self):
        return reverse("articles:index")

# create new article
class ArticleCreateView(SignupAsStaff, CreateView):
    model = Article 
    form_class = ArticleModelForm
    template_name = "articles/create_article.html"

    def get_success_url(self):
        return reverse("articles:index")

# signup
class SignupView(CreateView):
    form_class = CustomCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse("articles:login")

# about us
class AboutusPageView(TemplateView):
    template_name = "articles/about_us.html"
