from django.db import models

# Create your models here.

class Lehrender(models.Model):
    vorname = models.CharField(max_length=30)
    nachname = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default='null')

    def __str__(self):
        return f'{self.vorname} {self.nachname}'


class Student(models.Model):
    matrikel_nr = models.CharField(max_length=10)
    vorname = models.CharField(max_length=30)
    nachname = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default='null')

    def __str__(self):

        return f'{self.matrikel_nr} {self.vorname} {self.nachname} '

class Lehrveranstaltung(models.Model):
    name = models.CharField(max_length=30)
    lehrt = models.ForeignKey(Lehrender, on_delete=models.SET_NULL, null=True)
    besucht = models.ManyToManyField(Student)

    def __str__(self):
        a_string = ' , '.join([f'{a.name}' for a in self.besucht.all()])
        return f'{self.name} {self.lehrt} ({a_string})'


