import uuid
from django.db import models
from .baseModel import BaseModel


class Discussion(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.CharField(max_length=1022, null=False, blank=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)  # noqa: E501
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @classmethod
    def post_comment(cls, comment, user, lecture):
        discussion = Discussion(comment=comment, user=user, lecture=lecture)
        discussion.save()

        return discussion
