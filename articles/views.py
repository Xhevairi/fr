from django.contrib import messages
from django.shortcuts import render, reverse, redirect

# reset password
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# ./end reset password 

from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import SignupAsStaff, ArticleModelForm, CustomCreationForm
from .models import Article
import requests
from newsapp import settings

# reset password
DOMAIN_APP = settings.DOMAIN_APP
SITE_NAME_APP = settings.SITE_NAME_APP
PROTOCOL_APP = settings.PROTOCOL_APP
EMAIL_ADMIN = settings.EMAIL_ADMIN

# News API data
API_URL = settings.API_URL
country = settings.COUNTRY
API_KEY = settings.API_KEY

# validate query parameters
def is_valid_queryparam(param):
    return param != '' and param is not None

# get category
def get_category(request):
    category = request.GET.get('category')
    return (lambda x: category if category else '')(category)

# all news in french
def newsapi_all(request):
    category = get_category(request)
    url = f'{API_URL}={country}&apiKey={API_KEY}&category={category}'
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        articles = data['articles']
        return articles

# news by category
def newsapi(request):
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
    return render(request, 'articles/index.html', {
                                'news_api': news_api,
                                'articles': articles,
                            })

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
class ArticleUpdateView(SignupAsStaff, UpdateView):
    template_name = "articles/update_article.html"
    queryset = Article.objects.all()
    form_class = ArticleModelForm
    success_url = reverse_lazy('articles:index')

# delete article
class ArticleDeleteView(SignupAsStaff, DeleteView):
    template_name = "articles/delete_article.html"
    queryset = Article.objects.all() 
    success_url = reverse_lazy('articles:index')

# create new article
class ArticleCreateView(SignupAsStaff, CreateView):
    model = Article 
    form_class = ArticleModelForm
    template_name = "articles/create_article.html"
    success_url = reverse_lazy('articles:index')

# signup
class SignupView(CreateView):
    form_class = CustomCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('articles:login')

# about us
class AboutusPageView(TemplateView):
    template_name = "articles/about_us.html"

# reset password
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users:
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain': DOMAIN_APP,
                    'site_name': SITE_NAME_APP,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': PROTOCOL_APP,
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, EMAIL_ADMIN, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("/password_reset/done/")
            else:
                messages.error(request, 'An invalid email has been entered.')
                return redirect("/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})