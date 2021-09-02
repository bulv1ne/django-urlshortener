from django.urls import path

from . import views

app_name = "urlshortener"

urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("<str:word>/", views.ShortUrlRedirectView.as_view(), name="redirect"),
]
