from django.db import models

# Create your models here.

class Teacher(models.Model):
    id_teacher = models.IntegerField()
    nom = models.CharField()
    cognom = models.CharField()
    edat = models.IntegerField()
    rol= models.CharField()
    curs= models.CharField

class Student(models.Model):
    id_student = models.IntegerField()
    nom = models.CharField()
    rol = models.CharField()