from django.http import HttpResponse
from django.shortcuts import render
from app_familia.models import Familia
from app_familia.models import IngresoenSistema
from django.http import HttpResponse

# Create your views here.
#Para ver el inicio del html de la web#
def Inicio(request):
    return render(request,"plantilla.html")
#Para ver la BD de Familiar#
def Familiar(request):
    Familiar= Familia.object.all()
    #nombre= nommodelo#
    vista= loader.get_template('plantilla.html')
    vista= vista.render(Familiar)
    
    return HttpResponse(vista)
#Para ver la BD de Ingreso#
def Ingreso(request):
    Ingreso= IngresoenSistema.object.all()
    vista1= loader.get_template()#('plantilla.html')

    return HttpResponse(Ingreso)
#Para poder ingresar a nuestros familiares nuevos y la fecha de ingreso#
def ingresar_integrantes(request,nombre,apellido,parentesco,edad,direccion,email,check):

    familiar= Familia(nombre=Familia.Nombre,apellido=Familia.Apellido,parentesco=Familia.Parentesco,edad=Familia.Edad,direccion=Familia.Direccion,email=Familia.Email)
    familiar.save()
    ingresar=IngresoenSistema(nombre=IngresoenSistema.NomFam,check=IngresoenSistema.FamDirecto)
    ingresar.save()

    mensaje=f'Se guardó los datos de:{familiar.Nombre},con la fecha de ingreso de:{ingresar.FingresoSist},Para contacto mandar email a {familiar.Email}'
    return HttpResponse(mensaje)
