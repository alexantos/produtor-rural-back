from api.models import ModelBase

from django.db import models


class Safra(ModelBase):
    ano = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.ano