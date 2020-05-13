"""uebungDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Studentverwaltung.views import get_veranstaltung_list, get_home, get_student_list, get_lehrenden_list,\
    veranstaltung_details, student_details, lehrender_details, delete_lehrender, delete_lehrveranstaltungen,delete_studenten

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', get_home, name = 'home_page'),

    #Listen
    path('veranstaltungen/', get_veranstaltung_list, name = 'veranstaltung_list'),
    path('studenten/', get_student_list, name = 'student_list'),
    path('lehrenden/', get_lehrenden_list, name = 'lehrenden_list'),

    #Hinzufügen
    path('veranstaltung/add/', veranstaltung_details, name ='add_veranstaltung'),
    path('student/add/', student_details, name ='add_student'),
    path('lehrender/add/', lehrender_details, name ='add_lehrender'),

    #Editieren
    path('veranstaltung/edit/<int:pk>', veranstaltung_details, name ='edit_veranstaltung'),
    path('student/edit/<int:pk>', student_details, name ='edit_student'),
    path('lehrender/edit/<int:pk>', lehrender_details, name ='edit_lehrender'),

    #Löschen
    path('lehrender/<int:pk>', delete_lehrender, name ='delete_lehrender'),
    path('veranstaltung/<int:pk>', delete_lehrveranstaltungen, name ='delete_lehrveranstaltungen'),
    path('student/<int:pk>', delete_studenten, name ='delete_studenten'),

]
