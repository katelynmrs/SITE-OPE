from django.urls import path
from projeto.caixa import views as v


app_name = 'caixa'


urlpatterns = [
    path('', v.caixa_list, name='caixa_list'),
    path('<int:pk>/', v.caixa_detail, name='caixa_detail'),
    path('add/', v.CaixaCreate.as_view(), name='caixa_add'),
    path('<int:pk>/edit/', v.CaixaUpdate.as_view(), name='caixa_edit'),
    path('<int:pk>/json/', v.caixa_json, name='caixa_json'),
]
