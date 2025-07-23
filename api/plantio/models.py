from django.db import models

from api.cultura.models import Cultura
from api.models import ModelBase

from api.propriedade.models import Propriedade
from api.safra.models import Safra


class Plantio(ModelBase):
    cultura = models.ForeignKey(to=Cultura, on_delete=models.PROTECT)
    safra = models.ForeignKey(to=Safra, on_delete=models.PROTECT)
    propriedade = models.ForeignKey(to=Propriedade, on_delete=models.PROTECT)
    observacoes = models.TextField()