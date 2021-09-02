from django.test import TestCase
from django.urls import reverse

from ..models import ShortUrl, Word


class TestMainView(TestCase):
    def setUp(self):
        Word.objects.create(word="example")

    def test_fail(self):
        data = {
            "url": "invalid url",
        }
        self.client.post(reverse("urlshortener:index"), data)
        self.assertEqual(ShortUrl.objects.count(), 0)

    def test_success(self):
        data = {
            "url": "http://example.com",
        }
        self.client.post(reverse("urlshortener:index"), data)
        self.assertEqual(ShortUrl.objects.count(), 1)

    def test_no_words(self):
        Word.objects.all().delete()
        data = {
            "url": "http://example.com",
        }
        response = self.client.post(reverse("urlshortener:index"), data)
        self.assertEqual(response.status_code, 500)
