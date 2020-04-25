from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    def __str__(self):
        if self.__getattribute__('name'):
            return self.__getattribute__('name') #TODO: test if __getattributes__ or __getitem__ is useful

    # this is to make the class abstract so that django do not create table for it
    class Meta:
        abstract = True


class School(BaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, )
    established = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Standard(BaseModel):
    name = models.CharField(max_length=10)


class AcademicYear(BaseModel):
    name = models.CharField(max_length=10)


class Subject(BaseModel):
    name = models.CharField(max_length=100)


class Teacher(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name


class Student(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name


class Course(BaseModel):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Lecture(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)  # mention topics and etc here
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class LectureResource(BaseModel):
    name = models.CharField(max_length=100)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    types = [('V', 'Video'), ('A', 'Audio'), ('D', 'Document'), ('I', 'Image')]
    type = models.CharField(max_length=1, choices=types)
    link = models.URLField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


