from .baseModel import *


class Subject(BaseModel):
    name = models.CharField(max_length=100)
