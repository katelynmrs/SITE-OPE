from django.contrib import admin
from .models import Caixa


@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'funcionario',
        'salario',
        'horaextra',
    )
    search_fields = ('caixa',)
    list_filter = ('funcionario',)
