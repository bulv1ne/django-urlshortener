from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView
from django.views.generic.edit import FormView

from .exceptions import NoWordsAvailableException
from .forms import UrlForm
from .models import ShortUrl


class MainView(FormView):
    template_name = "urlshortener/index.html"
    form_class = UrlForm

    def form_valid(self, form):
        try:
            obj = ShortUrl.create_shorturl(url=form.cleaned_data["url"])
        except NoWordsAvailableException as e:
            # When there are no more words, a NoWordsAvailableException is raised
            return self.handle_exception(e, {"form": form})

        short_url = self.request.build_absolute_uri(obj.get_absolute_url())
        context = {
            "form": UrlForm(),
            "short_url": short_url,
        }
        return render(self.request, "urlshortener/index.html", context)

    def handle_exception(self, exception, context=None):
        if not context:
            context = {}
        context["error_message"] = str(exception)
        return render(self.request, "urlshortener/index.html", context, status=400)


class ShortUrlRedirectView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, word__word=kwargs["word"])
        return obj.url
