from api.models import ModelBase

from django.db import models

class Produtor(ModelBase):
	nome = models.CharField(max_length=128)
	cpf_cnpj = models.CharField(max_length=16)

	class Meta:
		verbose_name_plural = 'Produtores'