from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('students',views.index,name='index'),
    path('teachers',views.index,name='index'),
]