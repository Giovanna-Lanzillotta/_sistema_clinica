from django.contrib import admin

# Importação do módulo models.py
from sistema import models

# Register your models here.
# Aqui fica o registro do model do paciente.
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo')
    list_editable = ('ativo',)
    search_fields = ('id', 'nome', 'email',)