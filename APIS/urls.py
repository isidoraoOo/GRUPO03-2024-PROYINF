from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<int:pk>/', views.CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
    path('cities-list/', views.city_list_view, name='city-list'),
    path('map/', views.map, name='map')
]
