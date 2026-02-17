from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from apps.audit.application.use_cases import GetAuditLogsUseCase
from apps.audit.infrastructure.repositories import AuditLogRepository
from .serializers import AuditLogSerializer

class AuditLogListAPIView(ListAPIView):
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'action']
    ordering_fields = ['created_at', 'action']
    ordering = ['-created_at']

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        limit = int(self.request.query_params.get('limit', 100))
        
        use_case = GetAuditLogsUseCase(AuditLogRepository())
        audit_logs_entities = use_case.execute(user_id=int(user_id) if user_id else None, limit=limit)
        
        # Convert entities back to Django models for serializer compatibility
        from apps.audit.infrastructure.django_models import AuditLog
        return AuditLog.objects.filter(
            id__in=[log.id for log in audit_logs_entities]
        ).order_by('-created_at')
