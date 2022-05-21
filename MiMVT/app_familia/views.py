from django import db, views
from django.http import HttpResponse
from django.shortcuts import render
from app_familia.models import Familia
from app_familia.models import IngresoenSistema

# Create your views here.
#Para ver el inicio del html de la web#
def Inicios(request):
    return render(request,"plantilla.html")
#Para ver la BD de Familiar#
def Familiar(request):

    Familiar= Familia.object.all()
    #nombre= nommodelo#
    datos={"lista":Familiar}
    
    return render(request,"Familiares.html",datos)
#Para ver la BD de Ingreso#
def Ingreso(request):
    Ingreso= IngresoenSistema.object.all()

    listaF={"lista1":Ingreso}
    
    return render(request,"Ingreso.html",listaF)
#Para poder ingresar a nuestros familiares nuevos y la fecha de ingreso#
def ingresar_integrantes(request,nombre,apellido,parentesco,edad,direccion,email,check,familiar,ingresar):

    familiar=Familia.object.all()
    ingresar=IngresoenSistema.object.all()

    familiar= Familia(nombre='nombre',apellido='apellido',parentesco='parentesco',edad='edad',direccion='direccion',email='email')
    familiar.save()
    ingresar=IngresoenSistema(nombre='nombre',check='check')
    ingresar.save()

    

    return render(request,familiar,ingresar)
    mensaje=f'Se guardó los datos de:{familiar.Nombre},con la fecha de ingreso de:{ingresar.FingresoSist},Para contacto mandar email a {familiar.Email}'
    return HttpResponse(mensaje)
