from django.shortcuts import render

# Create your views here.
# Aqui fica a primeira view
def index(request):
    return render(
        request,
        'sistema/index.html'
    )

# REQUEST - RESPONSE - RENDER