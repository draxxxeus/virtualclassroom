import uuid
from django.utils.timezone import now
from datetime import datetime
from .baseModel import *
from .course import Course
from .resource import Resource


class Lecture(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chapter = models.CharField(max_length=7, default=None, null=True, blank=True)
    topic = models.CharField(max_length=126, default=None, null=True, blank=True)
    index = models.PositiveIntegerField(default=1, null=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)
    publish_on = models.DateTimeField(default=now, null=True, blank=True)
    complete_by = models.DateTimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @classmethod
    def get_lecture(cls, lecture_id, user):
        try:
            lecture = Lecture.objects.get(id=lecture_id)
            if lecture.course.standard == user.standard:
                recording = Resource.get_resources(lecture=lecture, type='R')[0]
                assignments = Resource.get_resources(lecture=lecture, type='A')

                prepared_lecture = {
                        'lecture': lecture,
                        'recording': recording,
                        'assignments': assignments
                }

                return prepared_lecture
            else:
                raise
        except Exception as e:
            return None

    @classmethod
    def get_lectures_for_user(cls, user, show_unpublished=False):
        try:
            courses = Course.get_courses_for_user(user)
            lectures = Lecture.objects.filter(course__in=courses).filter(publish_on__lte=datetime.now()).filter(complete_by__gte=datetime.now()).order_by('index')

            return {'lectures': list(lectures)}
        except:
            return None
