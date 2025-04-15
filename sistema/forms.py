from django import forms # Importa o módulo de Forms do django
from .models import Medico, Paciente # Importa o model Medico e Paciente

# Criando o form criado baseado no model Paciente (ModelForm)
class PacienteForm(forms.ModelForm):
    class Meta: # A classe Mete serve para configurar o form.
        model = Paciente # Define qual o model que o form representa
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'mensagem',]
        # fields são os campos que serão exibidos no form (HTML)

# Criando o form criado baseado no model Médico(ModelForm)
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'crm', 'email','telefone','mensagem','especialidade_id',]
        # labels = {
        #     'especialidade_id' : "Especialidade"
        # }