import uuid
from .baseModel import *
from .resource import Resource


class Lecture(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chapter = models.CharField(max_length=7, default=None, null=True, blank=True)
    topic = models.CharField(max_length=126, default=None, null=True, blank=True)
    index = models.PositiveIntegerField(default=1, null=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)
    publish_on = models.DateTimeField(default=None, null=True, blank=True)
    complete_by = models.DateTimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @classmethod
    def get_lecture(cls, lecture_id, user):
        try:
            lecture = Lecture.objects.get(id=lecture_id)
            if lecture.course.standard == user.standard:
                recording = Resource.get_resources(lecture=lecture, type='R')[0]
                notes = Resource.get_resources(lecture=lecture, type='A')

                prepared_lecture = {
                        'lecture': lecture,
                        'recording': recording,
                        'notes': notes
                }

                return prepared_lecture
            else:
                raise
        except Exception as e:
            return None
