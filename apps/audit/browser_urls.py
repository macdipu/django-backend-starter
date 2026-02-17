from django.urls import path
from .presentation.browser.views import AuditLogListView

urlpatterns = [
    path("logs/", AuditLogListView.as_view(), name="audit-logs-browser"),
]
