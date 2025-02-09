from django.shortcuts import render
from future.backports.http.client import HTTPResponse
from .models import Usuari
from .forms import EmailAuthenticationForm


# Create your views here.

def formulari(request):
    authentication_form = EmailAuthenticationForm
    return render(request, "loginform.html")

def ferlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    usuaris = Usuari.objects.all()
    for usuari in usuaris:
        if usuari.email==email and usuari.password == password:
            request.session["email"] = email
            request.session["password"] = password
            return HTTPResponse("Login correcte")

    return HTTPResponse("El usuari no existeix a la Base de dades")

def recuperarSessio(request):
    email = request.session.get("email")
    password = request.session.get("password")
    usuaris = Usuari.objects.all()
    for usuari in usuaris:
        if usuari.email==email and usuari.password == password:
            return render(request,"inicial.html",{'email':email,'password':password})

    return HTTPResponse("No tens la sessio iniciada")

def logout(request):
    request.session["email"] = ""
    request.session["password"]=""
    return render(request, "loginform.html")

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