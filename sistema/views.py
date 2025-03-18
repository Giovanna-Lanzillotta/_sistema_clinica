from django.shortcuts import render

# Create your views here.
# Aqui fica a primeira view
def index(request):
    return render(
        request,
        'global/base.html',
    )

# REQUEST - RESPONSE - RENDER

#exercicio view com meu nome
def seunome(request):
    return render(
        request,
        'global/seunome.html',
    )
