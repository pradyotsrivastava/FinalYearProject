from django.contrib.auth.forms import UserChangeForm
from phonenumber_field.modelfields import PhoneNumberField
from apps.member.models import User
from django.forms import ImageField

class CustomUserChangeForm(UserChangeForm):
    mobile_number=PhoneNumberField(region="IN")
    profile_image=ImageField()
    class Meta:
        model = User
        fields = ('name', 'mobile_number','profile_image')
        
    
