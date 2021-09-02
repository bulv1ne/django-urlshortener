from django.test import TestCase
from django.urls import reverse

from ..exceptions import NoWordsAvailableException
from ..models import ShortUrl, Word


class TestCreateShortUrl(TestCase):
    def setUp(self):
        Word.objects.create(word="something")
        Word.objects.create(word="example")

    def test_create_url(self):
        obj = ShortUrl.create_shorturl("http://example.com")
        self.assertEqual(obj.word.word, "example")

    def test_no_more_words(self):
        Word.objects.all().delete()
        with self.assertRaises(NoWordsAvailableException):
            ShortUrl.create_shorturl("http://example.com")


class TestRedirectShortUrl(TestCase):
    def setUp(self):
        word = Word.objects.create(word="example")
        ShortUrl.objects.create(word=word, url="http://example.com")

    def test_redirect(self):
        base_url = reverse("urlshortener:redirect", kwargs={"word": "example"})
        response = self.client.get(base_url, follow=False)
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, "http://example.com")
