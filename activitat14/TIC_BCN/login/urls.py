from django.urls import path
from . import views

urlpatterns = [
    path('formulari',views.formulari),
    path('ferLogin',views.ferlogin),
    path('inici',views.recuperarSessio),
    path('creaUsuari',views.guardarusuari),
]