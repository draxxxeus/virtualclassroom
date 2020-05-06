import uuid
from django.db import models
from .baseModel import BaseModel


class Discussion(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.CharField(max_length=1022, null=False, blank=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('Discussion', on_delete=models.CASCADE, default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @classmethod
    def get_discussions(cls, lecture):
        discussions = Discussion.objects.filter(lecture=lecture).order_by('-date_created')

        return discussions

    @classmethod
    def post_comment(cls, comment, user, lecture):
        discussion = Discussion(comment=comment, user=user, lecture=lecture)
        discussion.save()

        return discussion
