from typing import List
from ..domain.entities import AuditLogEntity
from .django_models import AuditLog

class AuditLogRepository:
    def save(self, audit_entity: AuditLogEntity) -> AuditLogEntity:
        audit_log = AuditLog.objects.create(
            user_id=audit_entity.user_id,
            action=audit_entity.action,
            metadata=audit_entity.metadata,
            ip_address=audit_entity.ip_address
        )
        return audit_log.to_entity()

    def get_logs(self, user_id: int = None, limit: int = 100) -> List[AuditLogEntity]:
        queryset = AuditLog.objects.all()
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        queryset = queryset.order_by('-created_at')[:limit]
        return [log.to_entity() for log in queryset]
