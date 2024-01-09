from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.home.models import BaseModel, City
from apps.member.models import User

# Create your models here.
class Ngo(BaseModel):
    registration_no = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()
    phone_no=PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    image = models.ImageField(upload_to='ngo\\banner')
    email = models.EmailField()

    def __str__(self):
        return self.name

    def ngo_list(self):
        return f'{self.name}-({self.purpose})'


class NgoBankDetails(BaseModel):
    ngo = models.OneToOneField(Ngo, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255, verbose_name="Account Holder's Name")
    bank_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ngo}-{self.account_no}-{self.ifsc_code}-{self.name}-{self.bank_name}'


# Ngo will reach you soon
# Auth user can fill this
class FundRaise(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255, verbose_name="Patient Name")
    prescription = models.ImageField(upload_to='ngo\\patient\\prescription',default="default.jpg")
    patient_address = models.CharField(max_length=255)
    reason = models.TextField()
    amount = models.DecimalField(max_digits=10,decimal_places=1)
    is_approved=models.BooleanField(verbose_name='Approved',default=False)
    is_raised=models.BooleanField(verbose_name="Raised Completed",default=False)
    def __str__(self):
        return f'{self.user}-{self.ngo}-{self.patient_name}-{self.prescription}-{self.patient_address}-{self.reason}-{self.amount}'


#donate for something else in future
#payment_gateway future
class Donate(BaseModel):
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Anonymous User", blank=True, verbose_name="Donar's Name")
    address = models.TextField()
    phone_no =PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    email = models.EmailField()  
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return f'{self.ngo}-{self.name}-{self.address}-{self.phone_no}-{self.email}-{self.amount}'


    