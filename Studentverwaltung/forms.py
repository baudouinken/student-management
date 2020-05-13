from django.forms import *
from Studentverwaltung.models import *

class LehrveranstaltungsForm(ModelForm):
    class Meta:
        model = Lehrveranstaltung
        exclude = ()
        labels = {'name' : 'Name der Lehrveranstaltung :',
                  'lehrt' : 'Gelehrt von : ',}

class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ()
        labels = {'matrikel_nr' : 'Matrikelnummer des Students :',
                  'besucht' : 'Lehrveranstaltung zu besuchen : ',}

class LehrenderForm(ModelForm):
    class Meta:
        model = Lehrender
        exclude = ()
        labels = {'vorname' : 'Vorname des Lehrenders :',
                  'nachname' : 'Nachname des Lehrenders : ',}
