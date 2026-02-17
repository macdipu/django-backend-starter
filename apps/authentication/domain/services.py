from ...users.infrastructure.repositories import UserRepository

class AuthenticationService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def authenticate(self, phone: str, password: str):
        user_entity = self.user_repo.get_by_phone(phone)
        if not user_entity or not user_entity.is_active:
            return None
        
        # In real implementation, verify password
        # For now, assume password is correct if user exists
        return user_entity

    def refresh_token(self, refresh_token: str):
        # Implement token refresh logic
        pass
