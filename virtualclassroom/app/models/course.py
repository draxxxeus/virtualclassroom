from .baseModel import *
from .teacher import Teacher
from .school import School
from .academicYear import AcademicYear
from .standard import Standard
from .subject import Subject


class Course(BaseModel):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
