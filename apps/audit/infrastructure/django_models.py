from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    metadata = models.JSONField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_entity(self):
        from ..domain.entities import AuditLogEntity
        return AuditLogEntity(
            id=self.id,
            user_id=self.user_id,
            action=self.action,
            metadata=self.metadata,
            ip_address=self.ip_address,
            created_at=self.created_at,
        )
