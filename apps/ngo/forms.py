from dataclasses import field
from django.forms import ModelForm
from apps.home.forms import forms
from .models import FundRaise
from .models import Donate

from apps.home.forms import name_characters_only


class FundRaiseForm(ModelForm):
    patient_name=forms.CharField(validators=[name_characters_only])
    class Meta:
        model=FundRaise
        fields=('ngo','patient_name','prescription','patient_address','reason','amount')

class DonateForm(ModelForm):
    name=forms.CharField(validators=[name_characters_only])
    class Meta:
        model=Donate
        fields=('ngo','name','address','phone_no','email','amount')

