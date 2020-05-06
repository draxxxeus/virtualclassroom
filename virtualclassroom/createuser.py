import factory
from factory.django import DjangoModelFactory
from app.models import User
from app.models import School
from app.models import Course
from datetime import datetime

teacher_template = 'testteacher{}@oneschool.pw'
student_template = 'teststudent{}@oneschool.pw'
school_name_template = 'Test School {}'
school_email_template = 'testschool{}@oneschool.pw'
password = 'pbkdf2_sha256$180000$3EPpD1Z7Nn7Z$sEq6A4SWttHmGvoFdvQSLWY0VHHFU7TKJ/PinNXlj6A='  # decoded: 1234


class StudentFactory(DjangoModelFactory):

    username = factory.Sequence(student_template.format)
    email = factory.Sequence(student_template.format)
    role = 'RO'
    standard = 'X'
    password = password

    class Meta:
        model = User


class TeacherFactory(DjangoModelFactory):

    username = factory.Sequence(teacher_template.format)
    email = factory.Sequence(teacher_template.format)
    role = 'RW'
    password = password

    class Meta:
        model = User


class SchoolFactory(DjangoModelFactory):

    name = factory.Sequence(school_name_template.format)
    email = factory.Sequence(school_email_template.format)
    phone = '12345678'
    address = 'Bangalore, India'

    class Meta:
        model = School


class CourseFactory(DjangoModelFactory):
    academic_year = '2020'
    standard = 'X'
    subject = 'History'
    textbook = '/a/b/c.pdf'

    class Meta:
        model = Course


def createObjects():
    school = SchoolFactory()
    teacher = TeacherFactory(school=school)
    student1 = StudentFactory(school=school, standard='X')
    student2 = StudentFactory(school=school, standard='XI')
    course = CourseFactory(teacher=teacher, standard='X', school=school)
    course = CourseFactory(teacher=teacher, standard='XI', school=school)

