from .baseModel import *


class AcademicYear(BaseModel):
    name = models.CharField(max_length=10)
