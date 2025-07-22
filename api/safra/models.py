from api.models import ModelBase

from django.db import models


class Safra(ModelBase):
    ano = models.PositiveIntegerField()
