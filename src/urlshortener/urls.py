from django.urls import include, path
from rest_framework import routers

from . import api_views, views

app_name = "urlshortener"

router = routers.DefaultRouter()
router.register("shorturl", api_views.CreateShortUrlViewSet)

urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("api/", include(router.urls)),
    path("<str:word>/", views.ShortUrlRedirectView.as_view(), name="redirect"),
]
