from django.shortcuts import render
from enterSources.models import Sources
from .utils import generar_resumen

def procesar_enlaces(request):
    enlaces = Sources.objects.all()

    for enlace in enlaces:
        if not enlace.resumen:  # Evitar procesar enlaces ya resumidos
            enlace.resumen = generar_resumen(enlace.link)
            enlace.save()

    return render(request, "procesar_enlaces.html", {"enlaces": enlaces})
