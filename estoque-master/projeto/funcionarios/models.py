from django.db import models
from django.contrib.auth.models import User
from ..departamentos.models import Departamento
from ..empresa.models import Empresa


class Funcionario(models.Model):
	nome = models.CharField(max_length=100)
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	departamentos = models.ManyToManyField(Departamento)
	empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
	
	

	def __str__(self):
		return self.nome
