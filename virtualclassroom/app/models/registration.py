import uuid

from django.db import models

from .baseModel import BaseModel


class Registration(BaseModel):
    USER_ROLES = [
            ('SU', 'institute_admin'),
            ('RW', 'faculty'),
            ('RO', 'student')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=14, default=None, null=True, blank=True)  # noqa: E501
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE, default=None, null=True, blank=True)  # noqa: E501
    user_role = models.CharField(max_length=2, choices=USER_ROLES, default='RO')  # noqa: E501
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
