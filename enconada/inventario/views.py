from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona, Arrendatario
from .form import PersonaForm, ArrendatarioForm
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("Hello World!!!!")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")
def personas(request):
    form = PersonaForm()
    persona = None
    id_Persona = request.GET.get("id")
    if id_Persona:
       persona = get_object_or_404(Persona, id=id_Persona)
       form = PersonaForm(instance=persona)
    if request.method =="POST":
        if persona:
           form = PersonaForm(request.POST, instance=persona)
        else:
           form = PersonaForm(request.POST)
    if form.is_valid():
        form.save()
    
    return render(request, "form_personas.html", {"form": form})

def arrendatarioFormView(request):
    form = ArrendatarioForm()
    arrendatario = None
    id_arrendatario = request.GET.get("id")
    if id_arrendatario:
        arrendatario = get_object_or_404(Arrendatario, id=id_arrendatario)
        form = ArrendatarioForm(instance=arrendatario)
    
    if request.method == "POST":
        if arrendatario:
            form = ArrendatarioForm(request.POST, instance=arrendatario)
        else:
            form = ArrendatarioForm(request.POST)
    
    if form.is_valid():
        form.save()
    
    return render(request, "form_arrendatario.html", {"form": form})