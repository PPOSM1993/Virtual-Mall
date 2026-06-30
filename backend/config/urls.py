from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema",
            template_name="drf_spectacular/swagger_ui.html",
        ),
        name="swagger-ui",
    ),

    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/booths/", include("apps.booths.urls")),
    path("api/companies/", include("apps.companies.urls")),
    path("api/categories/", include("apps.categories.urls")),
]