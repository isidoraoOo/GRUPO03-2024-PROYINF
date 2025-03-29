from django.urls import path
from . import views

urlpatterns = [    
    path('', views.archive, name='archive'), 
    path('main_entry/', views.main_entry, name='main_entry'),
]