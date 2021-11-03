from django.test import TestCase
from django.shortcuts import reverse

class ArticlesTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse('articles:articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/articles.html')