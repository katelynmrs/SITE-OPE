from django.contrib import admin
from .models import Caixa


@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'salario',
        'horaextra',
    )
    search_fields = ('nome',)
    list_filter = ('nome',)
