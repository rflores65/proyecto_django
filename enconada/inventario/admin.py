from django.contrib import admin
from .models import Persona, Arrendador, Arrendatario, Contrato
admin.site.register(Persona)
admin.site.register(Arrendador)
admin.site.register(Arrendatario)
admin.site.register(Contrato)

# Register your models here.
