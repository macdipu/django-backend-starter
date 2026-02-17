from .models import AuditLog

class AuditService:
    @staticmethod
    def log(user, action, metadata=None, ip=None):
        AuditLog.objects.create(
            user=user,
            action=action,
            metadata=metadata,
            ip_address=ip
        )
