from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from AnalysisBase.mixins import TimeStampMixin


class AnalystUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('Email is required for user creation')
        user = self.model(email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class AnalystUser(AbstractBaseUser, TimeStampMixin):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    email = models.EmailField(unique=True)

    # Profiling fields
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)

    is_staff = models.BooleanField(null=True)
    is_superuser = models.BooleanField(null=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return f'{self.email}, last logged in at {self.last_login}'
