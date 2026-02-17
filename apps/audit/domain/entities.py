from datetime import datetime
from typing import Optional, Any, Dict

class AuditLogEntity:
    def __init__(self, id: Optional[int], user_id: Optional[int], action: str, metadata: Optional[Dict[str, Any]] = None, ip_address: Optional[str] = None, created_at: Optional[datetime] = None):
        self.id = id
        self.user_id = user_id
        self.action = action
        self.metadata = metadata or {}
        self.ip_address = ip_address
        self.created_at = created_at or datetime.now()
