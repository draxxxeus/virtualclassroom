from .baseModel import *
from .course import Course

class Lecture(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)  # mention topics and etc here
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)