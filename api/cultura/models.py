from django.db import models

from api.models import ModelBase


class Cultura(ModelBase):
    descricao = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.descricao