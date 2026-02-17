from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from ..managers import UserManager

class Role(models.TextChoices):
    ADMIN = "ADMIN"
    SUPPORT = "SUPPORT"
    CUSTOMER = "CUSTOMER"
    AUDITOR = "AUDITOR"

class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "phone"

    def to_entity(self):
        from ..domain.entities import UserEntity
        return UserEntity(
            id=self.id,
            phone=self.phone,
            role=self.role,
            is_active=self.is_active,
            is_staff=self.is_staff,
            created_at=self.created_at,
        )

    def __str__(self):
        return self.phone
