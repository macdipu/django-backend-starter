from ..domain.services import AuthenticationService
from ...users.infrastructure.repositories import UserRepository

class LoginUseCase:
    def __init__(self, auth_service: AuthenticationService, user_repo: UserRepository):
        self.auth_service = auth_service
        self.user_repo = user_repo

    def execute(self, phone: str, password: str):
        return self.auth_service.authenticate(phone, password)

class RefreshTokenUseCase:
    def __init__(self, auth_service: AuthenticationService):
        self.auth_service = auth_service

    def execute(self, refresh_token: str):
        return self.auth_service.refresh_token(refresh_token)
