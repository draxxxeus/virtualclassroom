import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=14, default=None, null=True, blank=True)  # noqa: E501
    active_registration = models.ForeignKey('Registration', related_name='active_registration', on_delete=models.CASCADE, default=None, null=True, blank=True)  # noqa: E501

    def __repr__(self):
        return self.username

    def set_active_registration(self, registration=None):
        if not registration:
            registration = self.registration_set.first()

        self.active_registration = registration
        self.save()

    def as_dict(self):
        data = dict(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email
        )
        return data
