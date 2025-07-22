from api.models import ModelBase

from django.db import models

class Produtor(ModelBase):
	cpf_cnpj = models.CharField(max_length=16)
	nome = models.CharField(max_length=128)
