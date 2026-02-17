from .entities import UserEntity

class UserDomainService:
    @staticmethod
    def validate_phone(phone: str) -> bool:
        # Business rule: phone must be 10-15 digits
        return len(phone) >= 10 and len(phone) <= 15 and phone.isdigit()

    @staticmethod
    def can_user_perform_action(user: UserEntity, action: str) -> bool:
        if user.is_admin():
            return True
        # Add more business rules here
        return False
