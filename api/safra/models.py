from api.models import ModelBase

from django.db import models


class Safra(ModelBase):
    data_ano = models.PositiveIntegerField()
