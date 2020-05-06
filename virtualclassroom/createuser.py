import factory
from factory.django import DjangoModelFactory
from app.models import User
from app.models import School
from datetime import datetime

teacher_template = 'testteacher{}@oneschool.pw'
student_template = 'teststudent{}@oneschool.pw'
school_name_template = 'Test School {}'
school_email_template = 'testschool{}@oneschool.pw'
password = 'pbkdf2_sha256$180000$3EPpD1Z7Nn7Z$sEq6A4SWttHmGvoFdvQSLWY0VHHFU7TKJ/PinNXlj6A='  # decoded: 1234


class StudentFactory(DjangoModelFactory):

    username = factory.Sequence(student_template.format)
    email = factory.Sequence(student_template.format)

    password = password

    class Meta:
        model = User


class TeacherFactory(DjangoModelFactory):

    username = factory.Sequence(teacher_template.format)
    email = factory.Sequence(teacher_template.format)
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


school = SchoolFactory()
teacher = TeacherFactory()
student1 = StudentFactory()
student2 = StudentFactory()

