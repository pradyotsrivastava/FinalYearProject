from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .models import User
from apps.hospital.models import Hospital

class UserRegisterForm(UserCreationForm):
    mobile_number=PhoneNumberField(region="IN")
    class Meta:
        model = User
        fields = ('email', 'name', 'mobile_number')

class HospitalRegisterForm(ModelForm):
    class Meta:
        model=Hospital
        fields=('name','phone_no','license','image','address','city','pin')   
