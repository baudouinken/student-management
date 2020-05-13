from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
import sqlite3
from Studentverwaltung.forms import *

# Create your views here.
from Studentverwaltung.models import *

#home page
def get_home(request):

    return render(request, 'home.html', {'page_title' : 'Home page Studentverwaltung'})

#seiten mit Liste iher Objekten
def get_veranstaltung_list(request):
    veranstaltungen = Lehrveranstaltung.objects.all().order_by('name')

    return render(request, 'veranstaltung_list.html',
                  {'page_title':'Liste alle Lehrveranstaltungen',
                  'veranstaltungen':veranstaltungen})


def get_student_list(request):
    studenten = Student.objects.all().order_by('matrikel_nr')

    return render(request, 'student_list.html',
                            {'page_title' : 'Liste alle Studenten',
                             'studenten':studenten})


def get_lehrenden_list(request):
    lehrenden = Lehrender.objects.all().order_by('vorname')

    return render(request, 'lehrende_list.html',
                  {'page_tile':'Liste alle Lehrende',
                   'lehrenden':lehrenden})

#Edit Objekte
def veranstaltung_details(request, pk=None):
    if pk:
        veranstaltung = Lehrveranstaltung.objects.get(pk=pk)
    else:
        veranstaltung = Lehrveranstaltung()

    if request.method == 'POST':
        form = LehrveranstaltungsForm(request.POST, instance=veranstaltung)
        if form.is_valid():
            form.save()
            messages.success(request, 'Die Lehrveranstaltung wurde erfolgreich gespeichert')
            return HttpResponseRedirect(reverse_lazy('veranstaltung_list'))
    else:
        form = LehrveranstaltungsForm(instance = veranstaltung)

    return render(request, 'veranstaltung_details.html', {'page_title': 'Lehrveranstaltung hinzufügen',
                                                      'form':form})

def student_details(request, pk=None):
    if pk:
        student = Student.objects.get(pk=pk)
    else:
        student = Student()

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Der Student wurde erfolgreich gespeichert')
            return HttpResponseRedirect(reverse_lazy('student_list'))
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_details.html', {'page_title': 'Student hinzufügen',
                                                      'form': form})

def lehrender_details(request, pk=None):
    if pk:
        lehrender = Lehrender.objects.get(pk=pk)
    else:
        lehrender = Lehrender()

    if request.method == 'POST':
        form = LehrenderForm(request.POST, instance=lehrender)
        if form.is_valid():
            form.save()
            messages.success(request, 'Der Lehrende wurde erfolgreich gespeichert')
            return HttpResponseRedirect(reverse_lazy('lehrenden_list'))
    else:
        form = LehrenderForm(instance=lehrender)

    return render(request, 'lehrender_details.html', {'page_title': 'Lehrender hinzufügen',
                                                      'form': form})

#Lösche objekte
def delete_lehrender(request, pk):
    if pk:
        sup = Lehrender.objects.get(pk=pk)
        sup.delete()
        return HttpResponseRedirect(reverse_lazy('lehrenden_list'))

def delete_lehrveranstaltungen(request, pk):
    if pk:
        sup = Lehrveranstaltung.objects.get(pk=pk)
        sup.delete()
        return HttpResponseRedirect(reverse_lazy('veranstaltung_list'))

def delete_studenten(request, pk):
    if pk:
        sup = Student.objects.get(pk=pk)
        sup.delete()
        return HttpResponseRedirect(reverse_lazy('student_list'))


