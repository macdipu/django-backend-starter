from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from apps.audit.application.use_cases import GetAuditLogsUseCase
from apps.audit.infrastructure.repositories import AuditLogRepository

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


class AuditLogListView(AdminRequiredMixin, ListView):
    template_name = 'audit/audit_log_list.html'
    context_object_name = 'audit_logs'
    paginate_by = 50

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        limit = int(self.request.GET.get('limit', 100))
        
        use_case = GetAuditLogsUseCase(AuditLogRepository())
        audit_logs_entities = use_case.execute(user_id=int(user_id) if user_id else None, limit=limit)
        
        # Convert entities back to Django models for template compatibility
        from apps.audit.infrastructure.django_models import AuditLog
        return AuditLog.objects.filter(
            id__in=[log.id for log in audit_logs_entities]
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.GET.get('user_id')
        context['limit'] = self.request.GET.get('limit', 100)
        return context
