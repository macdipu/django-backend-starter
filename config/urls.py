from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from core.health import health_check, db_health_check, redis_health_check
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", lambda request: redirect("docs/")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("api/auth/", include("apps.authentication.urls")),
    path("api/audit/", include("apps.audit.api_urls")),  # API routes
    path("audit/", include("apps.audit.browser_urls")),  # Browser routes
    path("health/", health_check),
    path("health/db/", db_health_check),
    path("health/redis/", redis_health_check),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
