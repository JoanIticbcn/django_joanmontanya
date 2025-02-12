from django.shortcuts import render
from future.backports.http.client import HTTPResponse
from .models import Usuari
from .forms import EmailAuthenticationForm
from django.shortcuts import redirect


# Create your views here.

def formulari(request):
    authentication_form = EmailAuthenticationForm()
    context = {'form':authentication_form}
    return render(request, "loginform.html",context)

def ferlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    usuaris = Usuari.objects.all()
    for usuari in usuaris:
        if usuari.email==email and usuari.password == password:
            request.session["email"] = email
            request.session["password"] = password
            request.session["ID"] = usuari.id_usuari
            return redirect("inici")

    return HTTPResponse("Error: El usuari no existeix a la Base de dades o les credencials son erroneas")

def recuperarSessio(request):
    email = request.session.get("email")
    password = request.session.get("password")
    usuaris = Usuari.objects.all()
    for usuari in usuaris:
        if usuari.email==email and usuari.password == password:
            return render(request,"inicial.html",{'email':email,'password':password,'nom':usuari.nom})

    return HTTPResponse("Error: No tens la sessio iniciada o les credenciasl son erroneas")

def logout(request):
    request.session.flush()
    request.session.delete()
    return redirect('formulari')

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