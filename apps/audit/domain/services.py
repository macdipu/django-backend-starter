from .entities import AuditLogEntity

class AuditService:
    @staticmethod
    def should_log_action(action: str) -> bool:
        # Business rule: log only important actions
        important_actions = ["user_created", "user_deleted", "admin_action"]
        return action in important_actions
