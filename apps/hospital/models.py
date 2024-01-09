from django.db import models
from apps.home.models import BaseModel, City, Specialization
from apps.member.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Hospital(BaseModel):
    name = models.CharField(verbose_name='Hospital Name', max_length=255)
    phone_no=PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    license = models.FileField(upload_to='hospital//license')
    image = models.ImageField(upload_to='hospital//images')
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pin = models.PositiveIntegerField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HospitalInfo(BaseModel):
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    total_beds = models.PositiveIntegerField()
    remaining_beds = models.PositiveIntegerField()
    poison_cell = models.BooleanField(default=False)
    oxygen = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}-{self.hospital}-beds:{self.remaining_beds}'

class Treatment(BaseModel):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    diseases = models.TextField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,null=True,blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return f'{self.id}-{self.hospital}-{self.diseases}-{self.name}'
    

class HospitalAdmin(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.user}-{self.hospital}'


class Doctors(BaseModel):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    degree = models.CharField(max_length=255)
    degree_file = models.FileField(upload_to='hospital//doctors//degree')
    phone_no = PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    image = models.ImageField(upload_to='hospital//doctors//profile_images')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
