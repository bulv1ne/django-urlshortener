from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import ShortUrl, Word


class TestApi(APITestCase):
    def setUp(self):
        Word.objects.create(word="example")
        self.url = reverse("urlshortener:shorturl-list")

    def test_fail(self):
        data = {
            "url": "invalid url",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(ShortUrl.objects.count(), 0)

    def test_success(self):
        data = {
            "url": "http://example.com",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201, response.json())
        self.assertEqual(ShortUrl.objects.count(), 1)
        self.assertEqual(response.json()["short_url"], "http://testserver/example/")

    def test_no_words(self):
        Word.objects.all().delete()
        data = {
            "url": "http://example.com",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)
