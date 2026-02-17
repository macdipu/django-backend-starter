from django.urls import path, include

# Combined urlpatterns for backward compatibility
urlpatterns = [
    path("api/", include("apps.audit.api_urls")),
    path("", include("apps.audit.browser_urls")),
]
