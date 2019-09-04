from django.db import models
from django.urls import reverse_lazy
#from projeto.caixa.models import models
#from .managers import Funcionario, Salario

class Caixa(models.Model):
    funcionario = models.CharField(max_length=100, unique=True)
    salario = models.DecimalField('salario', max_digits=7, decimal_places=2)
    horaextra = models.IntegerField('hora extra')

    class Meta:
        ordering = ('funcionario',)

    def __str__(self):
        return self.caixa

    def get_absolute_url(self):
        return reverse_lazy('caixa:caixa_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'caixa': self.caixa,
        }
