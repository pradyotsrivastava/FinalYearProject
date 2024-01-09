from dataclasses import field
from django import forms
from .models import Cremation
import datetime
from apps.home.forms import name_characters_only


class CremationForm(forms.ModelForm):
    name=forms.CharField(validators=[name_characters_only])
    class Meta:
        model=Cremation
        fields=('religion','name','age','gender','address','demise_date','demise_time','demise_city','is_priest','is_vehicle')
        widgets = {
            'demise_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'demise_time': forms.TimeInput( attrs={'class':'form-control', 'placeholder':'Select a time', 'type':'time'}),
        }
    
    def clean_demise_date(self,*args,**kwargs):
        value=self.cleaned_data.get("demise_date")
        curr_date=datetime.date.today()
        pre_date=datetime.date.today() - datetime.timedelta(days=1)
        if value==curr_date or value==pre_date:
            return value
        else:
            raise forms.ValidationError("Please enter valid demsie date, either today or yesterday")
    
    


