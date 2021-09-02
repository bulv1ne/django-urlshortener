from django.db import models
from django.urls import reverse

from .exceptions import NoWordsAvailableException
from .utils import word_regex


class WordManager(models.Manager):
    def find_close_match(self, url):
        for word in word_regex.findall(url.lower()):
            obj = self.unused_words().filter(word=word).first()
            if obj:
                return obj
        obj = self.unused_words().order_by("?").first()
        if obj:
            return obj
        raise NoWordsAvailableException("No more words available")

    def unused_words(self):
        return self.filter(shorturl=None)


class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)

    objects = WordManager()

    def __str__(self):
        return self.word


class ShortUrl(models.Model):
    url = models.URLField(unique=True)
    word = models.OneToOneField("Word", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("urlshortener:redirect", kwargs={"word": self.word})

    @classmethod
    def create_shorturl(self, url):
        obj = ShortUrl.objects.filter(url=url).first()
        if obj:
            return obj
        return ShortUrl.objects.create(url=url, word=Word.objects.find_close_match(url))

    def __str__(self):
        return f"{self.word} <{self.url}>"
