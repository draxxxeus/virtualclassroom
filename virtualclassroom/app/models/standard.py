import uuid

from django.db import models

from .baseModel import BaseModel


class Standard(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=14)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    __str__ = __repr__

    def as_dict(self):
        data = dict(
            name=self.name,
            institution=self.institution.as_dict()
        )
        return data