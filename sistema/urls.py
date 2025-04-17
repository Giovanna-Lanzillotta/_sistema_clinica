#urls.py do sistema
from django.urls import path

# Importação do diretorio views.py, onde tem a view index e a view listarPaciente
from sistema import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pacientes/',views.listarPacientes,name='pacientes'),
    path('pacientes/novo', views.criarPacientes, name='criar_pacientes'),
    path('pacientes/perfil/<int:paciente_id>',views.perfilPaciente,name='perfil_paciente'),
    path('medicos/',views.listarMedicos,name='medicos'),
    path('medicos/novo/', views.criarMedicos, name='criar_medicos')
    
   
]
