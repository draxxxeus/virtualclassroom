import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLES = [
            ('SU', 'institute_admin'),
            ('RW', 'faculty'),
            ('RO', 'student')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=14, default=None, null=True, blank=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE, default=None, null=True)
    standard = models.CharField(max_length=14, default=None, null=True, blank=True)
    role = models.CharField(max_length=2, choices=USER_ROLES, default='RO')
