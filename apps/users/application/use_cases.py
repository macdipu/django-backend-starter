from ..domain.entities import UserEntity
from ..domain.services import UserDomainService
from ..infrastructure.repositories import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, phone: str, role: str = "CUSTOMER") -> UserEntity:
        if not UserDomainService.validate_phone(phone):
            raise ValueError("Invalid phone number")
        
        # Check if user exists
        if self.user_repo.get_by_phone(phone):
            raise ValueError("User already exists")
        
        # Create user
        user = UserEntity(id=None, phone=phone, role=role)
        return self.user_repo.save(user)

class GetUserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, phone: str) -> UserEntity:
        user = self.user_repo.get_by_phone(phone)
        if not user:
            raise ValueError("User not found")
        return user
