from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from .models import Caixa
from .forms import CaixaForm


def caixa_list(request):
    template_name = 'caixa_list.html'
    objects = Caixa.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)

class CaixaList(ListView):
    model = Caixa
    template_name = 'caixa_list.html'
    paginate_by = 10
    
def caixa_detail(request, pk):
    template_name = 'caixa_detail.html'
    obj = Caixa.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def caixa_add(request):
    template_name = 'caixa_form.html'
    return render(request, template_name)

class CaixaCreate(CreateView):
    model = Caixa
    template_name = 'caixa_form.html'
    form_class = CaixaForm


class CaixaUpdate(UpdateView):
    model = Caixa
    template_name = 'caixa_form.html'
    form_class = CaixaForm


def caixa_json(request, pk):
    caixa = Caixa.objects.filter(pk=pk)
    data = [nome.to_dict_json() for nome in caixa]
    return JsonResponse({'data': data})
