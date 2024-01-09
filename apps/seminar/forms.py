from dataclasses import field
from django import forms
from .models import SeminarAttendees
from apps.home.forms import name_characters_only

class SeminarAttendeesForms(forms.ModelForm):
    name=forms.CharField(validators=[name_characters_only])
    class Meta:
        model=SeminarAttendees
        fields=('name','age','mobile_no','email')
    
    
