from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, password=None, **kwargs):

        if not nickname:
            raise ValueError('must have user nickname')

        user = self.model(
            nickname=nickname,
            **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password=None, **kwargs):

        user = self.create_user(
            nickname=nickname,
            password=password,
            **kwargs,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    nickname = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'nickname'

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.nickname
