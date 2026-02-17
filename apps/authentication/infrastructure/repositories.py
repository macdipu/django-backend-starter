from typing import Protocol, Optional
from ...users.domain.entities import UserEntity

class TokenService(Protocol):
    def generate_access_token(self, user: UserEntity) -> str:
        ...

    def generate_refresh_token(self, user: UserEntity) -> str:
        ...

    def validate_token(self, token: str) -> Optional[UserEntity]:
        ...

class JWTTokenService:
    def generate_access_token(self, user: UserEntity) -> str:
        # JWT token generation logic
        from rest_framework_simplejwt.tokens import AccessToken
        access_token = AccessToken.for_user(user)
        return str(access_token)

    def generate_refresh_token(self, user: UserEntity) -> str:
        # JWT refresh token generation logic
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh_token = RefreshToken.for_user(user)
        return str(refresh_token)

    def validate_token(self, token: str) -> Optional[UserEntity]:
        # Token validation logic
        from rest_framework_simplejwt.tokens import AccessToken
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            # Get user from repository
            from ...users.infrastructure.repositories import UserRepository
            user_repo = UserRepository()
            return user_repo.get_by_id(user_id)
        except Exception:
            return None
