from django.db import models


class BaseModel(models.Model):
    def __str__(self):
        if self.__getattribute__('id'):
            # TODO: test if __getattributes__ or __getitem__ is useful
            return str(self.__getattribute__('id'))

    # make the class abstract so that django do not create table for it
    class Meta:
        abstract = True
