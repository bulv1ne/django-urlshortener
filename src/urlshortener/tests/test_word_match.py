from django.test import TestCase

from ..exceptions import NoWordsAvailableException
from ..models import ShortUrl, Word


class TestWordMatch(TestCase):
    def setUp(self):
        Word.objects.create(word="something")
        Word.objects.create(word="example")

    def test_match(self):
        obj = Word.objects.find_close_match("http://example.com/")
        self.assertEqual(obj.word, "example")

    def test_match_already_used(self):
        example_word = Word.objects.get(word="example")
        ShortUrl.objects.create(word=example_word, url="http://my.example.com")

        obj = Word.objects.find_close_match("http://example.com/")
        self.assertEqual(obj.word, "something")

    def test_no_match(self):
        obj = Word.objects.find_close_match("http://facebook.com/")
        self.assertNotEqual(obj.word, "facebook")

    def test_no_more_words(self):
        Word.objects.all().delete()
        with self.assertRaises(NoWordsAvailableException):
            Word.objects.find_close_match("http://example.com/")
