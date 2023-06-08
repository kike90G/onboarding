from django.shortcuts import render
from django.http import HttpResponse

# Vistas planONB
# Create your views here.
#solo imprime un texto html
def inicio(request):
    #return HttpResponse("<h1>Bienvenido Onboarding</h1>")
    return render(request, 'paginas/inicio.html')

#aqui mandamos a llamar el archivo html
def nosotros(request):
    return render(request, 'paginas/nosotros.html')



#acceso a las paginas de empleado
def empleado(request):
    return render(request, 'empleado/index.html')

def crear(request):
    return render(request, 'empleado/crear.html')

def editar(request):
    return render(request, 'empleado/editar.html')

