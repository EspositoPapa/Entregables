from django.urls import path
from app_familia.models import IngresoenSistema #config de url#
from.import views

urlpatterns = [
    path("Inicio/",views.Inicio)
    path("Familiar/",views.Familia),
    path("Ingreso/",views.IngresoenSistema),
    path("ingresar_integrantes/",views.ingresar_integrantes),
]