import uuid
from .baseModel import *
from .school import School
from .user import User


class Course(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=124)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=14)
    standard = models.CharField(max_length=14)
    subject = models.CharField(max_length=30)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
