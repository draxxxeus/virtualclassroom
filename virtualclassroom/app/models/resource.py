import uuid
from .baseModel import *
from .lecture import Lecture
from .user import User


class Resource(BaseModel):
    RESOURCE_CHOICES = [
            ('A', 'Assignment'),
            ('R', 'Recording'),
            ('N', 'Notes'),
            ('O', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=124)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=RESOURCE_CHOICES)
    link = models.URLField(max_length=512)
    publish_on = models.DateTimeField()
    complete_by = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
