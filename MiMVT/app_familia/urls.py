from django.urls import path

from MiMVT.app_familia.models import IngresoenSistema #config de url#
from.import views

urlpatterns = [
    path("Familiar/",views.Familia),
    path("Ingreso/",views.IngresoenSistema),
    path("ingresar_integrantes/",views.familiar,view.Ingreso),
]