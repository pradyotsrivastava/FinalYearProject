from django.db import models
from apps.home.models import BaseModel
from apps.home.models import City
from apps.member.models import User
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class FixedCharges(BaseModel):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return f'{self.name}-{self.amount}'


class Religion(BaseModel):
    name = models.CharField(max_length=255)
    material_cost = models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return self.name
    

class Vehicle(BaseModel):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    vehicle_no = models.CharField(max_length=255)
    driver_name = models.CharField(max_length=255)
    phone_no = PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    def __str__(self):
        return f'{self.city}-{self.vehicle_no}-{self.driver_name}-{self.phone_no}'
    

class Priest(BaseModel):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_no = PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.religion}-{self.name}-{self.phone_no}-{self.address}-{self.city}'


class Cremation(BaseModel):
    GENDER = (
        ('M','Male'),
        ('F','Female'),
        ('T','Transgender'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER, default='M', max_length=1)
    address = models.CharField(max_length=255)
    demise_date = models.DateField()
    demise_time = models.TimeField()
    demise_city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    is_priest = models.BooleanField(default=False)
    is_vehicle = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    is_paid = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user}-{self.religion}-{self.name}-{self.age}-{self.gender}-{self.address}-{self.demise_date}-{self.demise_time}-{self.is_priest}-{self.is_vehicle}-{self.amount}'

