from typing import Optional
from ..domain.entities import UserEntity
from .django_models import User

class UserRepository:
    def get_by_phone(self, phone: str) -> Optional[UserEntity]:
        try:
            user = User.objects.get(phone=phone)
            return user.to_entity()
        except User.DoesNotExist:
            return None

    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        try:
            user = User.objects.get(id=user_id)
            return user.to_entity()
        except User.DoesNotExist:
            return None

    def save(self, user_entity: UserEntity) -> UserEntity:
        if user_entity.id:
            user = User.objects.get(id=user_entity.id)
            user.phone = user_entity.phone
            user.role = user_entity.role
            user.is_active = user_entity.is_active
            user.is_staff = user_entity.is_staff
            user.save()
        else:
            user = User.objects.create_user(
                phone=user_entity.phone,
                role=user_entity.role,
                is_active=user_entity.is_active,
                is_staff=user_entity.is_staff
            )
        return user.to_entity()

    def delete(self, user_id: int) -> bool:
        try:
            User.objects.get(id=user_id).delete()
            return True
        except User.DoesNotExist:
            return False
