from django.db import models
from apps.home.models import BaseModel
from apps.member.models import User
from apps.cremation.models import Cremation
from apps.seminar.models import Seminar
from apps.ngo.models import Ngo
from apps.hospital.models import Hospital
from apps.hospital.models import Doctors

def rating_scale():
    value=((i,i) for i in range(1,11))
    return value

# Create your models here.
class FeedbackCremation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cremation = models.ForeignKey(Cremation, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=rating_scale())
    description = models.CharField(max_length=255)
    suggestion = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f'{self.user}-{self.cremation}-{self.rating}'

class FeedbackNgo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=rating_scale())
    description = models.CharField(max_length=255)
    suggestion = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
            return f'{self.user}-{self.ngo}-{self.rating}'

class FeedbackSeminar(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=rating_scale())
    description = models.CharField(max_length=255)
    suggestion = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f'{self.user}-{self.seminar}-{self.rating}'



class FeedbackHospital(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=rating_scale())
    description = models.CharField(max_length=255)
    suggestion = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f'{self.user}-{self.hospital}-{self.rating}'


    
class FeedbackDoctor(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=rating_scale())
    description = models.CharField(max_length=255)
    suggestion = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f'{self.user}-{self.doctor}-{self.rating}'

   
