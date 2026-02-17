from datetime import datetime
from typing import Optional

class TokenPair:
    def __init__(self, access_token: str, refresh_token: str, expires_in: Optional[int] = None):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in or 3600  # Default 1 hour
        self.created_at = datetime.now()

    @property
    def is_expired(self) -> bool:
        # Simple expiration check (in real implementation, decode JWT)
        return False  # Placeholder
