from django.db import models
from django.urls import reverse_lazy
#from projeto.caixa.models import models
#from .managers import nome, Salario

class Caixa(models.Model):
    nome = models.CharField('Nome',max_length=80, unique=True)
    salario = models.DecimalField('Salário', max_digits=7, decimal_places=2)
    horaextra = models.PositiveIntegerField('Hora extra')

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome #m


    def get_absolute_url(self):
        return reverse_lazy('caixa:caixa_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'caixa': self.nome, #m
        }

