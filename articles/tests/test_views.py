from django.test import TestCase
from django.shortcuts import reverse
from articles.models import Article

class ArticlesTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            category = "Sport",
            title = "New Era",
            authors = "from newspapers",
            content = "A lot to be done in all sport activities",
            authors_image = "media/images/team-1.jpg",
            content_image = "media/images/team-1.jpg",
            # created_at = models.DateTimeField(auto_now_add=True)
            slug = "New-Era"
        )

    def test_get(self):
        response = self.client.get(reverse('articles:articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/articles.html')

    def test_article_content(self):
        self.assertEqual(self.article.category, "Sport")
        self.assertEqual(self.article.content, "A lot to be done in all sport activities")
        

    