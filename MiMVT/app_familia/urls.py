from django import views
import sqlite3
from django.urls import path
from app_familia.models import IngresoenSistema #config de url#
from app_familia.models import Familia
from app_familia.views import Inicios
from app_familia.views import Familiar
from app_familia.views import Ingreso
from app_familia.views import ingresar_integrantes

from.import views

urlpatterns = [
    path("Inicio/",views.Inicios),
    path("Familiar/",views.Familiar),
    path("Ingreso/",views.Ingreso),
    path("ingresar_integrantes/<nombre>",views.ingresar_integrantes),
]