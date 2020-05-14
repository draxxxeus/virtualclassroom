import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=14, default=None, null=True, blank=True)  # noqa: E501
    active_registration = models.ForeignKey('Registration', related_name='active_registration', on_delete=models.CASCADE, default=None, null=True, blank=True)  # noqa: E501

    @classmethod
    def set_active_registration(cls, request, registration=None):
        if not registration:
            registration = request.user.registration_set.all()[0]

        request.user.active_registration = registration
        request.user.save()
