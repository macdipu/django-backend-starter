from django.urls import path
from .presentation.api.views import AuditLogListAPIView

urlpatterns = [
    path("logs/", AuditLogListAPIView.as_view(), name="audit-logs"),
]
