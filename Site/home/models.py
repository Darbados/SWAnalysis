from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from Site.mixins import TimeStampMixin


class AnalystUser(AbstractBaseUser, TimeStampMixin):
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}, last logged in at {self.last_login}'
