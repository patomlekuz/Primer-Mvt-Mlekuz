from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Context, Template, loader

def familia(request):
    
    familia1=Familia(nombre="Hector", apellido="Valdez",edad=15)
    familia.save()
   
    diccionario={"nombre":familia.nombre,"apellido":familia.apellido,"edad":familia.edad}
    
    plantilla=loader.get_template("template1.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)


