import uuid
import os
import logging
from django.db import models
from ..utils.vimeo import Vimeo

from .baseModel import BaseModel

logger = logging.getLogger()


def get_resource_path(instance, filename):
    return 'lectures/{0}/{1}/{2}'.format(instance.lecture_id, instance.type, filename)  # noqa: E501


class Resource(BaseModel):
    RESOURCE_CHOICES = [
            ('A', 'Assignments'),
            ('R', 'Recording'),
            ('O', 'Other')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media = models.FileField(upload_to=get_resource_path)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=RESOURCE_CHOICES)
    link = models.URLField(max_length=512, default=None, null=True, blank=True)
    publish_on = models.DateTimeField(default=None, null=True, blank=True)
    complete_by = models.DateTimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def as_dict(self):
        data = dict(
            id=self.id,
            type=self.type,
            link=self.link
        )
        return data

    def upload_to_vimeo(self):
        relative_path_on_filesystem = self.media.url.strip('/')
        file_path = os.path.join(os.getcwd(), relative_path_on_filesystem)
        vimeo = Vimeo()
        link = vimeo.upload(file_path)
        self.link = link

    @classmethod
    def get_resources_for_lecture(cls, lecture_id):
        try:
            resources = Resource.objects.filter(lecture=lecture_id)
            return resources
        except Exception as e:
            logger.exception("Returning empty list because error occurred while fetching lectures for course: {}"
                             .format(lecture_id))
            return []
