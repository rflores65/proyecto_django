from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>/', views.contact , name='contact'),
    path('personas/', views.personas, name='personas'),
    path('arrendatario/', views.arrendatarioFormView, name="arrendatario"),
    path('saludo/', views.index),
]
