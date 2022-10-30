from django.contrib import admin

from personas.models import Persona,Domicilio

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)