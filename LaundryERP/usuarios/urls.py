from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('emp/', views.index_empleado, name='index_empleado'),
    path('cli/', views.index_cliente, name='index_cliente'),
]
