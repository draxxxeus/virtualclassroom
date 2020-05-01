import uuid
from .baseModel import *
from .course import Course
from .user import User


class Lecture(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chapter = models.CharField(max_length=7, default=None, null=True, blank=True)
    topic = models.CharField(max_length=126, default=None, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_on = models.DateTimeField(default=None, null=True, blank=True)
    complete_by = models.DateTimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
