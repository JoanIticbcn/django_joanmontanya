from django.urls import path
from . import views

urlpatterns = [
    path('login',views.guardarsessio),
    path('inici',views.recuperarsessio)
]