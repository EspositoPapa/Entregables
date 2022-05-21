from django.urls import path
from app_familia.models import IngresoenSistema #config de url#
from app_familia.models import Familia
from.import views

urlpatterns = [
    path("Inicio/",views.Inicios),
    path("Familiar/",views.Familiar),
    path("Ingreso/",views.Ingreso),
    path("ingresar_integrantes/",views.ingresar_integrantes),
]