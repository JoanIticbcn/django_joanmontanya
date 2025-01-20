from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Teacher

# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def insertTeacher():
    teacher = Teacher(
        id_teacher=1,
        nom="Oriol",
        cognom="Roca",
        edat=34,
        rol="profe",
        curs="2n de daw"
    )
    teacher.save()
    return HttpResponse("Insert teacher successfull")

def insertStudent():
    student = Student(
        id_student=1,
        nom="Joan",
        rol="Estudiant",
    )
    student.save()
    return HttpResponse("Insert Successfull")

def getTeachers():
    teachers = Teacher.objects.all()
    return ""

def getStudents():
    students = Student.objects.all()
    return ""