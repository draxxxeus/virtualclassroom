import uuid
from .baseModel import *
from .lecture import Lecture
from .user import User


class Resource(BaseModel):
    RESOURCE_CHOICES = [
            ('A', 'Assignments'),
            ('R', 'Recording'),
            ('O', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.FileField(upload_to='uploads/')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=RESOURCE_CHOICES)
    link = models.URLField(max_length=512, default=None, null=True, blank=True)
    publish_on = models.DateTimeField(default=None, null=True, blank=True)
    complete_by = models.DateTimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
