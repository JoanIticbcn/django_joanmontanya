from django.shortcuts import render
from future.backports.http.client import HTTPResponse
from .models import Usuari
from .forms import EmailAuthenticationForm


# Create your views here.

def ferlogin(request):
    authentication_form = EmailAuthenticationForm
    email = request.POST.get('email')
    password = request.POST.get('password')
    if (email and password) and (Usuari.email==email and Usuari.password==password):
        request.session["email"] = email
        request.session["password"] = password
        return render(request,"loginform.html")
    else:
        return HTTPResponse("El usuari no existeix a la Base de dades")

def recuperarSessio(request):
    email = request.session.get("email")
    password = request.session.get("password")
    if (email and password) and (Usuari.email==email and Usuari.password==password):
        return render(request,"inicial.html",{'email':email,'password':password})
    else:
        return HTTPResponse("No tens la sessio iniciada")

def guardarusuari():
    usuari = Usuari(
        id_usuari = 1,
        email = "joan@itibcn.cat",
        nom = "Joan",
        password = 1234,
        cognom = "Montanya"
    )
    usuari.save()
    return HTTPResponse("Usuari creat correctament")