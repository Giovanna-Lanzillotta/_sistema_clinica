# Django

# Comandos principais

1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> venv\Scripts\activate
3. Instalar o django no projeto -> pip install django
4. Para criar um projeto Django -> django-admin startproject project .
5. Para subir o servidor -> python manage.py runserver
6. Para criar um novo app -> python manage.py startapp sistema
7. Para criar um superuser -> python manage.py createsuperuser
8. Para alterar a senha caso você esqueça -> python manage.py changepassword nomedousuario
9. Para instalar o pillow no projeto -> python -m pip install PIllow
10. Para gerar o pacote de migração -> python manage.py makemigrations
11. Para rodar as alterações desse pacote -> python manage.py migrate
12. Para coletar todos os arquivos estáticos do projeto -> python manage.py collectstatic

# PRINCIPAIS ARQUIVOS/PASTAS DO PROJECT

1. settings.py -> é o arquivo de configuração do projeto.
2. urls.py -> é o arquivo base[principal] de urls do projeto.


# DOCUMENTAÇÃO 

1. `urls` -> https://docs.djangoproject.com/en/5.1/topics/http/urls/
2. `settings` - > https://docs.djangoproject.com/en/5.1/topics/settings/ , https://docs.djangoproject.com/en/5.1/ref/settings/


# Criação das entidades do sistema

[PACIENTE]
nome
sobrenome
email
telefone
criação
mensagem
ativo
imagem

[ESPECIALIDADE]
ortopedia
cardiologia
neurologia
clinico geral

[MEDICO]
nome
sobrenome
crm
email
data do cadastro do médico
telefone
imagem
ativo
mensagem

[CONSULTA]

[ENDEREÇO]

# Criar uma view que vai redenderizar um arquivo chamado seu nome.html
# No seunome.html coloque um h1 com o seu nome
# Em seguida, crie uma url e chame esse arquivo seunome.html

## AULA DO DIA 08/04/2025

1. INJEÇÃO DE CONTEXTO -> Utilizando o dicionário `contex` para acessar todos os objetos
- class Paciente(Modelo - Tabela)
- acessar todos os objetos(instâncias) que foram criadas a partir da classe Paciente.
- Renderizar todos esses contatos no arquivo listar.html

## AULA DO DIA 17/04/2025

# METODOLOGIAS ÁGEIS

- CASCADE -> tradicional,apresenta o projeto final ao cliente,o cliente não participa de nenhuma etapa.
escolhe um framework de metodologias ágeis para utilizar
- KABAN
- XP
- LUNA
- STAR
- # SCRUM # scrum master é um facilitador
- `daily` - acontece todo dia uma reunião. dura de 10 a 15 minutos. falar como esta sua tarefa.momento de pedir ajuda.ver as tarefas em aberto, ver datas de entrega,
- `sprint` - aninhamento inicial do projeto,reunião 15 a 15 dias ou 1 vez por mês, presença de todo mundo da equipe, `backlog` (escolher as ações que vão ser feitas), Dura de uma hora
a uma hora e meia.
- `sprint review` - é a entrega. Dura de uma hora a uma hora e meia.
- `refinamento` - ver o que deu certo e o que pode melhorar. uma vez por mês de uma hora a uma hora e meia.

## AULA DO DIA 24/04/2025

1. Incluir alguns comandos no settings.py para tratar a imagem
2. Ir no urls.py e incluir uma rota dinâmica para as imagens
3. Ir no listar.html e incluir o campo imagem