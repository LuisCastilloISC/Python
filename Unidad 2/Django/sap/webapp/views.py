from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Persona
# Create your views here.
def bienvenido(request):
    noPersonas=Persona.objects.count()
#    personas= Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request,'bienvenido.html',{'noPersonas': noPersonas,'personas':personas})

def despedirse(request):
    return HttpResponse('Despedida desde DJango')

def contacto(request):
    return HttpResponse('un correo')
