#urls.py do sistema
from django.urls import path

# Importação do diretorio views.py, onde tem a view index e a view listarPaciente
from sistema import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pacientes/',views.listarPacientes,name='pacientes'),
    path('medicos/',views.listarMedicos,name='medicos'),
   
]
