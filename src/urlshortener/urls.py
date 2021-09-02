from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers

from . import api_views, views

app_name = "urlshortener"

router = routers.DefaultRouter()
router.register("shorturl", api_views.CreateShortUrlViewSet)

urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("api/", include(router.urls)),
    path("r/<str:word>/", views.ShortUrlRedirectView.as_view(), name="redirect"),
    # Schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="urlshortener:schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="urlshortener:schema"),
        name="redoc",
    ),
]
