from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.Persons, name="Persons"),

]
