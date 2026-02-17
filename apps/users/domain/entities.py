from datetime import datetime
from typing import Optional

class UserEntity:
    def __init__(self, id: Optional[int], phone: str, role: str, is_active: bool = True, is_staff: bool = False, created_at: Optional[datetime] = None):
        self.id = id
        self.phone = phone
        self.role = role
        self.is_active = is_active
        self.is_staff = is_staff
        self.created_at = created_at or datetime.now()

    def is_admin(self) -> bool:
        return self.role == "ADMIN"

    def can_access_audit(self) -> bool:
        return self.role in ["ADMIN", "AUDITOR"]
