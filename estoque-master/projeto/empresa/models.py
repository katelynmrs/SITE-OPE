from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='nome da empresa',unique=True)

    def __str__(Self):
        return str(self.nome)