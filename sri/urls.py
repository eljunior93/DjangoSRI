from django.urls import path
from .views import crearEmpresa

urlpatterns = [
   path('crear_empresa/',crearEmpresa, name='crear_empresa')
]