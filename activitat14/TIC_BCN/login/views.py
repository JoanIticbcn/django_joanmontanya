from django.shortcuts import render

# Create your views here.

def guardarsessio(request):
    request.session["user"] = "Joan"
    return render(request,"login.html")

def recuperarsessio(request):
    user = request.session.get("user")
    return render(request,"inici.html",{'user':user})