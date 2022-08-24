from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Context, Template, loader

def familia(request):
    
    familia=Familia(nombre="Hector", apellido="Valdez",edad=15)
    familia.save()
    familia_1=Familia(nombre="Raul", apellido="Guitos",edad=40)
    familia_1.save
    familia_2=Familia(nombre="Micaela", apellido="Cubito",edad=35)
    familia_2.save
    diccionario={"nombre":familia.nombre,"apellido":familia.apellido,"edad":familia.edad,
    "nombre_1":familia_1.nombre,"apellido_1":familia_1.apellido,"edad_1":familia_1.edad,
    "nombre_2":familia_2.nombre,"apellido_2":familia_2.apellido,"edad_2":familia_2.edad}
    lista_nombres=[familia.nombre,familia_1.nombre,familia_2.nombre]
    lista_apellidos=[familia.apellido,familia_1.apellido,familia_2.apellido]
    lista_edades=[familia.edad,familia_1.edad,familia_2.edad]
    
    
    plantilla=loader.get_template("template1.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)


