from django.db import models
from django.contrib.auth.models import AbstractUser
from .school import School
from .standard import Standard


class User(AbstractUser):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, default=None, null=True)
    standard = models.ForeignKey(Standard, null=True, on_delete=models.SET_NULL, default=None)
