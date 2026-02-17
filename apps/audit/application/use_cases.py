from ..domain.entities import AuditLogEntity
from ..domain.services import AuditService
from ..infrastructure.repositories import AuditLogRepository

class LogActionUseCase:
    def __init__(self, audit_repo: AuditLogRepository):
        self.audit_repo = audit_repo

    def execute(self, user_id: int, action: str, metadata: dict = None, ip_address: str = None):
        if not AuditService.should_log_action(action):
            return
        
        audit_log = AuditLogEntity(
            id=None,
            user_id=user_id,
            action=action,
            metadata=metadata,
            ip_address=ip_address
        )
        self.audit_repo.save(audit_log)

class GetAuditLogsUseCase:
    def __init__(self, audit_repo: AuditLogRepository):
        self.audit_repo = audit_repo

    def execute(self, user_id: int = None, limit: int = 100):
        return self.audit_repo.get_logs(user_id=user_id, limit=limit)
