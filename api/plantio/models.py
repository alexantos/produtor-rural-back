from django.db import models

from api.cultura.models import Cultura
from api.models import ModelBase

from api.propriedade.models import Propriedade
from api.safra.models import Safra


class Plantio(ModelBase):
    cultura = models.ForeignKey(to=Cultura, on_delete=models.CASCADE)
    safra = models.ForeignKey(to=Safra, on_delete=models.CASCADE)
    propriedade = models.ForeignKey(to=Propriedade, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)