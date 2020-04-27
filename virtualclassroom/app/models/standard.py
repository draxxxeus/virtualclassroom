from .baseModel import *


class Standard(BaseModel):
    name = models.CharField(max_length=10)
