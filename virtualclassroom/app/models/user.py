import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .school import School


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=14)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None, null=True)
    standard = models.CharField(max_length=14, default=None, null=True)
