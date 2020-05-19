import uuid

from django.db import models

from .baseModel import BaseModel


class Institution(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=126)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=254)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def as_dict(self):
        data = dict(
            name=self.name,
            email=self.email,
            phone=self.phone,
            address=self.address
        )
        return data 