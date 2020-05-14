import factory
from factory.django import DjangoModelFactory
from app.models import Course, Institution, Lecture, Registration, Resource, Standard, User  # noqa: E501

teacher_email_template = 'teacher{}@oneschool.pw'
student_email_template = 'student{}@oneschool.pw'
institution_name_template = 'Institution {}'
institution_email_template = 'institute{}@oneschool.pw'
chapter_template = '{}'
topic_template = '{}'
password = 'pbkdf2_sha256$180000$3EPpD1Z7Nn7Z$sEq6A4SWttHmGvoFdvQSLWY0VHHFU7TKJ/PinNXlj6A='  # decoded: 1234  # noqa: E501


class CourseFactory(DjangoModelFactory):

    class Meta:
        model = Course


class InstitutionFactory(DjangoModelFactory):
    name = factory.Sequence(institution_name_template.format)
    email = factory.Sequence(institution_email_template.format)
    phone = '12345678'
    address = 'Bangalore, India'

    class Meta:
        model = Institution


class LectureFactory(DjangoModelFactory):
    chapter = factory.Sequence(chapter_template.format)
    topic = factory.Sequence(topic_template.format)

    class Meta:
        model = Lecture


class RegistrationFactory(DjangoModelFactory):

    class Meta:
        model = Registration


class ResourceFactory(DjangoModelFactory):

    class Meta:
        model = Resource


class StandardFactory(DjangoModelFactory):

    class Meta:
        model = Standard


class StudentFactory(DjangoModelFactory):
    username = factory.Sequence(student_email_template.format)
    email = factory.Sequence(student_email_template.format)
    password = password

    class Meta:
        model = User


class TeacherFactory(DjangoModelFactory):
    username = factory.Sequence(teacher_email_template.format)
    email = factory.Sequence(teacher_email_template.format)
    password = password

    class Meta:
        model = User


def createObjects():
    # create 3 institutions
    institution1 = InstitutionFactory()
    institution2 = InstitutionFactory()
    institution3 = InstitutionFactory()

    # create 3 teachers and 5 students
    teacher1 = TeacherFactory()
    teacher2 = TeacherFactory()
    teacher3 = TeacherFactory()

    student1 = StudentFactory()
    student2 = StudentFactory()
    student3 = StudentFactory()
    student4 = StudentFactory()
    student5 = StudentFactory()

    # add standards for each institution
    standard_i1_ix = StandardFactory(name='IX', institution=institution1)
    standard_i1_x = StandardFactory(name='X', institution=institution1)

    standard_i2_ix = StandardFactory(name='IX', institution=institution2)
    standard_i2_x = StandardFactory(name='X', institution=institution2)

    standard_i3_x = StandardFactory(name='X', institution=institution3)

    # register teachers and students to institution
    RegistrationFactory(user=teacher1, institution=institution1, user_role='RW')  # noqa: E501
    RegistrationFactory(user=teacher2, institution=institution1, user_role='RW')  # noqa: E501

    RegistrationFactory(user=teacher2, institution=institution2, user_role='RW')  # noqa: E501
    RegistrationFactory(user=teacher3, institution=institution2, user_role='RW')  # noqa: E501

    RegistrationFactory(user=teacher1, institution=institution3, user_role='RW')  # noqa: E501

    RegistrationFactory(user=student1, institution=institution1, standard=standard_i1_x, user_role='RO')  # noqa: E501
    RegistrationFactory(user=student2, institution=institution1, standard=standard_i1_x, user_role='RO')  # noqa: E501
    RegistrationFactory(user=student3, institution=institution1, standard=standard_i1_x, user_role='RO')  # noqa: E501
    RegistrationFactory(user=student4, institution=institution1, standard=standard_i1_ix, user_role='RO')  # noqa: E501
    RegistrationFactory(user=student5, institution=institution1, standard=standard_i1_ix, user_role='RO')  # noqa: E501

    RegistrationFactory(user=student1, institution=institution2, standard=standard_i2_x, user_role='RO')  # noqa: E501
    RegistrationFactory(user=student2, institution=institution2, standard=standard_i2_x, user_role='RO')  # noqa: E501
    RegistrationFactory(user=student4, institution=institution2, standard=standard_i2_x, user_role='RO')  # noqa: E501
    RegistrationFactory(user=student5, institution=institution2, standard=standard_i2_ix, user_role='RO')  # noqa: E501

    RegistrationFactory(user=student3, institution=institution3, standard=standard_i3_x, user_role='RO')  # noqa: E501

    # define courses
    c_i1_ix_phy = CourseFactory(subject='Physics', standard=standard_i1_ix, teacher=teacher1)  # noqa: E501
    c_i1_ix_che = CourseFactory(subject='Chemistry', standard=standard_i1_ix, teacher=teacher1)  # noqa: E501
    c_i1_ix_mat = CourseFactory(subject='Mathematics', standard=standard_i1_ix, teacher=teacher2)  # noqa: E501
    c_i1_x_phy = CourseFactory(subject='Physics', standard=standard_i1_x, teacher=teacher1)  # noqa: E501
    c_i1_x_mat = CourseFactory(subject='Mathematics', standard=standard_i1_x, teacher=teacher2)  # noqa: E501

    c_i2_ix_mat = CourseFactory(subject='Mathematics', standard=standard_i2_ix, teacher=teacher2)  # noqa: E501
    c_i2_x_mat = CourseFactory(subject='Mathematics', standard=standard_i2_x, teacher=teacher3)  # noqa: E501

    c_i3_x_phy = CourseFactory(subject='Physics', standard=standard_i3_x, teacher=teacher1)  # noqa: E501
    c_i3_x_che = CourseFactory(subject='Chemistry', standard=standard_i3_x, teacher=teacher1)  # noqa: E501

    # create lectures
    l_i1_ix_phy_1 = LectureFactory(course=c_i1_ix_phy, teacher=teacher1)
    l_i1_ix_che_1 = LectureFactory(course=c_i1_ix_che, teacher=teacher1)
    l_i1_ix_mat_1 = LectureFactory(course=c_i1_ix_mat, teacher=teacher2)

    l_i1_x_phy_1 = LectureFactory(course=c_i1_x_phy, teacher=teacher1)
    l_i1_x_mat_1 = LectureFactory(course=c_i1_x_mat, teacher=teacher2)

    l_i2_ix_mat_1 = LectureFactory(course=c_i2_ix_mat, teacher=teacher2)
    l_i2_x_mat_1 = LectureFactory(course=c_i2_x_mat, teacher=teacher3)

    l_i3_x_phy_1 = LectureFactory(course=c_i3_x_phy, teacher=teacher1)
    l_i3_x_che_1 = LectureFactory(course=c_i3_x_che, teacher=teacher1)

    ResourceFactory(lecture=l_i1_ix_phy_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501
    ResourceFactory(lecture=l_i1_ix_che_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501
    ResourceFactory(lecture=l_i1_ix_mat_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501
    ResourceFactory(lecture=l_i1_x_phy_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501
    ResourceFactory(lecture=l_i1_x_mat_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501

    ResourceFactory(lecture=l_i2_ix_mat_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501
    ResourceFactory(lecture=l_i2_x_mat_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501

    ResourceFactory(lecture=l_i3_x_phy_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501
    ResourceFactory(lecture=l_i3_x_che_1, type='R', link='https://vimeo.com/416826723')  # noqa: E501
