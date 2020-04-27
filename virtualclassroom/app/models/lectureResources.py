from .baseModel import *
from .lecture import Lecture
from .teacher import Teacher


class LectureResource(BaseModel):
    name = models.CharField(max_length=100)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    types = [('V', 'Video'), ('A', 'Audio'), ('D', 'Document'), ('I', 'Image')]
    type = models.CharField(max_length=1, choices=types)
    link = models.URLField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
