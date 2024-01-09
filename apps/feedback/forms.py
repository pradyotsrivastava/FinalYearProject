from django.forms import ModelForm
from .models import *

class FeedbackCremationForm(ModelForm):
    class Meta:
        model=FeedbackCremation
        fields=('cremation','rating','description','suggestion')

class FeedbackDoctorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FeedbackDoctorForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['doctor'].queryset = Doctors.objects.all().order_by('name')
    class Meta:
        model=FeedbackDoctor
        fields=('doctor','rating','description','suggestion')

class FeedbackNgoForm(ModelForm):
    class Meta:
        model=FeedbackNgo
        fields=('ngo','rating','description','suggestion')

class FeedbackSeminarForm(ModelForm):
    class Meta:
        model=FeedbackSeminar
        fields=('seminar','rating','description','suggestion')

class FeedbackHospitalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FeedbackHospitalForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['hospital'].queryset = Hospital.objects.filter(is_verified=True).order_by('name')
    class Meta:
        model=FeedbackHospital
        fields=('hospital','rating','description','suggestion')
