import factory
from factory.django import DjangoModelFactory
from app.models import User, Institution, Course, Lecture, Resource, Standard, Registration
from datetime import datetime, timedelta

teacher_template = 'testteacher{}@oneinstitution.pw'
student_template = 'teststudent{}@oneinstitution.pw'
institution_name_template = 'Test Institution {}'
institution_email_template = 'testinstitution{}@oneinstitution.pw'
chapter_name_template = 'testchapter{}'
course_topic_template = 'testchaptertopic{}'
standard_name_template = 'testStandard{}'
password = 'pbkdf2_sha256$180000$3EPpD1Z7Nn7Z$sEq6A4SWttHmGvoFdvQSLWY0VHHFU7TKJ/PinNXlj6A='  # decoded: 1234


class StandardFactory(DjangoModelFactory):
    name = factory.Sequence(standard_name_template.format)

    class Meta:
        model = Standard


class StudentFactory(DjangoModelFactory):

    username = factory.Sequence(student_template.format)
    email = factory.Sequence(student_template.format)
    password = password

    class Meta:
        model = User


class RegistrationFactory(DjangoModelFactory):

    class Meta:
        model = Registration


class TeacherFactory(DjangoModelFactory):

    username = factory.Sequence(teacher_template.format)
    email = factory.Sequence(teacher_template.format)
    password = password

    class Meta:
        model = User


class InstitutionFactory(DjangoModelFactory):

    name = factory.Sequence(institution_name_template.format)
    email = factory.Sequence(institution_email_template.format)
    phone = '12345678'
    address = 'Bangalore, India'

    class Meta:
        model = Institution


class CourseFactory(DjangoModelFactory):
    academic_year = '2020'
    standard = 'X'
    subject = 'History'
    textbook = '/a/b/c.pdf'

    class Meta:
        model = Course


class LectureFactory(DjangoModelFactory):
    chapter = factory.Sequence(chapter_name_template.format)
    topic = factory.Sequence(course_topic_template.format)
    complete_by = datetime.now() + timedelta(weeks=104)

    class Meta:
        model = Lecture


def createObjects():
    institution = InstitutionFactory()
    standard1 = StandardFactory(institution=institution)
    standard2 = StandardFactory(institution=institution)
    teacher = TeacherFactory()
    teacher_reg = RegistrationFactory(user=teacher, institution=institution, user_role='RW')
    student1 = StudentFactory()
    student1_reg = RegistrationFactory(user=student1, institution=institution, user_role='RO')
    student2 = StudentFactory()
    student2_reg = RegistrationFactory(user=student2, institution=institution, user_role='RO')
    course1 = CourseFactory(teacher=teacher, standard=standard1)
    lecture11 = LectureFactory(teacher=teacher, course=course1)
    course2 = CourseFactory(teacher=teacher, standard=standard2)
    lecture21 = LectureFactory(teacher=teacher, course=course2)
