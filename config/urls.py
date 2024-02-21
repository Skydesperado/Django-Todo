from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.todo.urls")),
    path("authentication/", include("apps.authentication.urls")),
    path("oauth/", include("allauth.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema")),
    path("api/schema/swagger/",
         SpectacularSwaggerView.as_view(url_name="schema")),
    path("rosetta/", include("rosetta.urls")),
]
