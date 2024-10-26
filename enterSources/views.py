from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from enterSources.models import Sources
from enterSources.forms import Bulletin_request

# Create your views here.

def home(request):
    return render(request, "index.html")

def service(request):
    if request.method == 'POST':
        form1 = Bulletin_request(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Fuente agregada exitosamente.')
            return redirect('../result_insert/')  # Redirigir a una página de éxito o lista
    else:
        messages.error(request, 'Hubo un error al agregar la fuente. Por favor, revisa los campos.')
        form1 = Bulletin_request()
    
    return render(request, 'insert.html', {'form': form1})

def result_insert(request):
    return HttpResponse("Exito al ingresar la fuente de datos.")