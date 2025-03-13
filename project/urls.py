"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#urls.py do project 
# São as importações realizadas de forma a utilizar partes do Django.
from django.contrib import admin
from django.urls import path, include

# Lista resposnsável por organizar as urls do sistema.
urlpatterns = [
    path('', include('sistema.urls')),
    path('admin/', admin.site.urls),
]

# path() -> É um método do django que permite realizar a inserção de uma url.
