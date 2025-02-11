from django.db import models

# Create your models here.
class Usuari(models.Model):
    id_usuari = models.AutoField(primary_key=True)
    email = models.CharField(unique=True)
    nom = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)