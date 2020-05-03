import uuid
from .baseModel import *


class Course(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=14)
    standard = models.CharField(max_length=14)
    subject = models.CharField(max_length=30)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    @classmethod
    def get_courses(cls, user_id):
        courses = Course.objects.filter(teacher=user_id)

        return courses

    @classmethod
    def get_courses_for_user(cls, user):
        try:
            courses = Course.objects.filter(standard=user.standard)

            return list(courses)
        except:
            return None
