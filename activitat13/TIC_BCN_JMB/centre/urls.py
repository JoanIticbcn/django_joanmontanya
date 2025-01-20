from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index),
    path('students',views.getTeachers),
    path('teachers',views.getStudents),
    path('teachers/insert',views.insertTeacher),
    path('students/insert',views.insertStudent),
]