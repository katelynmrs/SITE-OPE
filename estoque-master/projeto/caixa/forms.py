from django import forms
from .models import Caixa


class CaixaForm(forms.ModelForm):

    class Meta:
        model = Caixa
        fields = '__all__'
