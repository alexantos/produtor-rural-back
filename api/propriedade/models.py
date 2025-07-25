from api.models import ModelBase

from django.db import models

from api.produtor.models import Produtor
from api.propriedade.choices import ESTADOS


class Propriedade(ModelBase):
    nome = models.CharField(max_length=128)
    produtor = models.ForeignKey(to=Produtor, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=2, choices=ESTADOS)
    area_total_fazenda = models.DecimalField(max_digits=6, decimal_places=1)
    area_agricultavel = models.DecimalField(max_digits=6, decimal_places=1)
    area_vegetacao = models.DecimalField(max_digits=6, decimal_places=1)


    def __str__(self):
        return self.nome