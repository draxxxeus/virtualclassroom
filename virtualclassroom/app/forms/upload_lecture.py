from django.forms import ModelForm
from ..models import Lecture, Resource

class UploadLectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = ['course', 'chapter', 'topic', 'course', 'publish_on', 'complete_by']
