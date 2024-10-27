from django.urls import path
from enterSources import views

urlpatterns = {
    path('', views.home),
    path('insert/', views.service),
    path('result_insert/', views.result_insert),
}