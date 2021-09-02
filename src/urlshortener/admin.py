from django.contrib import admin

from .models import ShortUrl, Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_select_related = ("word",)
    raw_id_fields = ("word",)
    list_display = (
        "word",
        "url",
    )
