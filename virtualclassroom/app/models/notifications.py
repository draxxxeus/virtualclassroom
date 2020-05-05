import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Content, Mail, Personalization

from .user import User


class Notifications():

    @classmethod
    def new_lecture_notification(cls, lecture):
        students = User.objects.filter(standard=lecture.course.standard, role='RO')
        student_emails = [student.email for student in students]
        lecture_url = "https://oneschool.pw/lecture/?id={0}".format(lecture.id)

        mail = Mail()
        mail.from_email = Email("noreply@oneschool.pw", "Notification")
        mail.subject = "New lecture added for {0}".format(lecture.course.subject)
        mail.add_content(Content("text/html", ("Visit <a href='{0}'>this link</a> to see the new lecture.".format(lecture_url))))

        personalization = Personalization()
        personalization.add_to(Email(lecture.teacher.email))
        for email in student_emails:
            personalization.add_bcc(Email(email))

        mail.add_personalization(personalization)
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        try:
            sg.client.mail.send.post(request_body=mail.get())
        except Exception.BadRequestsError as e:
            print(e)

    @classmethod
    def send_email(cls, to, subject, body):
        mail = Mail(
            from_email="noreply@oneschool.pw",
            to_emails=to,
            subject=subject,
            html_content=body
        )

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(mail)
            return response
        except Exception as e:
            return None
