import requests
from django.shortcuts import render
from rest_framework import generics
from .models import City
from .serializers import CitySerializer

# Create your views here.

# Vista para listar todas las ciudades o crear una nueva
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Vista para obtener, actualizar o eliminar una ciudad específica
class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

def city_list_view(request):
    # URL de la API local o el endpoint donde obtienes la lista de ciudades
    api_url = 'http://127.0.0.1:8000/api/cities/'
    
    # Realiza la solicitud GET a la API para obtener los datos
    response = requests.get(api_url)
    
    # Verifica que la respuesta sea exitosa
    if response.status_code == 200:
        cities = response.json()  # convierte la respuesta en formato JSON a un diccionario de Python
    else:
        cities = []  # si la solicitud falla, usa una lista vacía para evitar errores en la plantilla

    # Pasa los datos de las ciudades a la plantilla
    return render(request, 'city_list.html', {'cities': cities})

def map(request):
    return render(request, 'TEST1.html')