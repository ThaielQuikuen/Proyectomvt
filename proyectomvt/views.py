from re import template
from urllib import request
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
import random

from home.models import Familiar





# def crear_familiar(request):
    
#     familiar1 = Familiar(nombre='Carolina', apellido='Fuii',edad=45,fecha_craecion=datetime.now())
#     familiar2 = Familiar(nombre='Milagros', apellido='Segura',edad=20,fecha_craecion=datetime.now())
#     familiar3 = Familiar(nombre='Kevin', apellido='Quikuen',edad=22,fecha_craecion=datetime.now())
#     familiar1.save()
#     familiar2.save()
#     familiar3.save()
#     template = loader.get_template('crearfamiliar.html')
#     template_renderizado = template.render()
#     return HttpResponse(template_renderizado)

def crear_familiar(request,nombre,apellido):
    familiar = Familiar(nombre=nombre,apellido=apellido,edad=random.randrange(1,99),fecha_craecion=datetime.now())
    familiar.save()
    template = loader.get_template('crearfamiliar.html')
    template_renderizado = template.render({'familiar':familiar})
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    familiar = Familiar.objects.all()

    template = loader.get_template('verfamiliares.html')
    template_renderizado = template.render({'familiar':familiar})
    return HttpResponse(template_renderizado)