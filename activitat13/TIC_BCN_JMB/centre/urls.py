from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index),
    path('students',views.getStudents,name='students'),
    path('teachers',views.getTeachers,name='teachers'),
    path('teachers/insert',views.insertTeacher),
    path('students/insert',views.insertStudent),
]