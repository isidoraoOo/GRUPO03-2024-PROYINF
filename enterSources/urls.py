from django.urls import path
from enterSources import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('insert/', views.service, name='insert'), 
    path('result_insert/', views.result_insert, name='result_insert'),
    path('select/', views.select, name='select')
]
