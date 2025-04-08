#urls.py do sistema
from django.urls import path

# Importação do diretorio views.py, onde tem a view index e a view listarPaciente
from sistema import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('listar/',views.listarPacientes,name='listar'),
    path('medicos/',views.listarMedicos,name='medicos'),
   
]
