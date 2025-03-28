from django.urls import path
from . import views

urlpatterns = [
    path('', views.procesar_enlaces, name='procesar_enlaces'),
]
