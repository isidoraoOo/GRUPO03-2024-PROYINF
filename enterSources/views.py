from django.shortcuts import render
from django.http import HttpResponse
from enterSources.models import Sources

# Create your views here.

def home(request):
    return HttpResponse("Inicio")

def service(request):
    return render(request, "index.html")

def enter_source(request):
    source = request.GET.get("source", None)
    sources = []

    if(request.GET["source"]):
        message = "Fuente a ingresar: %r" %request.GET["source"]
        source = request.GET["source"]

        sources = Sources.object.filter(__name__icontains=source)
    else:
        message = "No se ha introducido fuentes."

    return render(request, "result_insert.html", {"sources":sources, "query":source, "message":message})

def home(request):
    return HttpResponse("Inicio")

def home(request):
    return HttpResponse("Inicio")