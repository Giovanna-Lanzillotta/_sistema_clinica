# Importação do módulo models que traz métodos do banco de dados
from django.db import models

# Importação do módulo timezone que trás datas e horários
from django.utils import timezone

# Create your models here.
# Aqui fica o model do paciente
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='img/%Y%m/')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

