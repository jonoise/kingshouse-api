from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken


class MainUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if not email:
            raise ValueError('Email Required')

        if not password:
            raise ValueError('Password Required')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.username = username
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('Email Required')

        if not password:
            raise ValueError('Password Required')

        super_user = self.create_user(email, password=password)
        super_user.is_admin = True
        super_user.is_staff = True
        super_user.is_active = True
        super_user.save(using=self._db)
        return super_user


class MainUser(AbstractBaseUser):

    email = models.EmailField('email address', name='email', unique=True)
    name = models.CharField(max_length=64)
    is_owner = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # AUTOMATIC
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = MainUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
