import uuid
from .baseModel import *


class School(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=126)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=254)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
