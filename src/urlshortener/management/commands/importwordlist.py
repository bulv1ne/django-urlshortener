from django.core.management.base import BaseCommand

from urlshortener.models import Word
from urlshortener.utils import cleanup_wordlist


class Command(BaseCommand):
    help = "Imports a wordlist into the database"

    def add_arguments(self, parser):
        parser.add_argument("wordlist_files", nargs="+", type=open)

    def handle(self, *args, **options):
        for wordlist_file in options["wordlist_files"]:
            self.stdout.write("Importing words from {}".format(wordlist_file.name))
            Word.objects.bulk_create(
                (Word(word=word) for word in cleanup_wordlist(wordlist_file)),
                ignore_conflicts=True,
            )
