from django.urls import include, path
from projeto.core import views as v




app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
]
