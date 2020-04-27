from .baseModel import *


class School(BaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, )
    established = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)