from django.db import models

from api.models import ModelBase

from api.propriedade.models import Propriedade
from api.safra.models import Safra


class Cultura(ModelBase):
    descricao = models.CharField(max_length=64)
    safra = models.ForeignKey(to=Safra, on_delete=models.PROTECT)
    propriedade = models.ForeignKey(to=Propriedade, on_delete=models.PROTECT)
