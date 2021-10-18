from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    HEALTH = 'HL'
    ACTUALITY = 'ACT'
    SPORT = 'SP'
    POLITICS = 'POL'
    BUSINESS = 'BNS'
    ENTERTAINMENT = 'ENTM'
    HISTORY = 'HS'
    LITERATURE = 'LTR'
    CATEGORY_ARTICLE_CHOICES = [
        (HEALTH, 'Health'),
        (ACTUALITY, 'Actuality'),
        (SPORT, 'Sport'),
        (POLITICS, 'Politics'),
        (ENTERTAINMENT, 'Entertainment'),
        (HISTORY, 'History'),
        (LITERATURE, 'Literature'),
    ]
    category = models.CharField(
        max_length=4,
        choices=CATEGORY_ARTICLE_CHOICES,
        default=ACTUALITY,
    )
    title = models.CharField(max_length=1024)
    authors = models.CharField(max_length=1024)
    content = models.TextField()
    authors_image = models.ImageField(upload_to='images/', max_length=100, null=True, blank=True)
    content_image = models.ImageField(upload_to='images/', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=1024, null=True, blank=True)


    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title

    def is_upperclass(self):
        return self.category in {self.ACTUALITY, self.LITERATURE}
    
    @property
    def authors_image_url(self):
        if self.authors_image and hasattr(self.authors_image, 'url'):
            return self.authors_image.url
        else:
            return "/static/img/authors_default_image.jpg"

    @property
    def content_image_url(self):
        if self.content_image and hasattr(self.content_image, 'url'):
            return self.content_image.url
        else:
            return "/static/img/content_default_image.jpg"