from django.db import models
from apps.home.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Seminar(BaseModel):
    MODE = (
        ("Online", "Online"),
        ("Offline", "Offline"),
    )
    speaker = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(auto_now=False)
    start_at = models.TimeField()
    duration = models.DecimalField(max_digits=7,decimal_places=2)
    mode = models.CharField(max_length=10, choices=MODE, default='Online')
    venue = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='seminar\\cover_image', default='seminar.jpg')
    watch_on_url = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f'{self.speaker}-{self.title}-{self.description}-{self.date}-{self.start_at}-{self.duration}-{self.mode}-{self.venue}-{self.cover_image}-{self.watch_on_url}'


class SeminarAttendees(BaseModel):
    seminar=models.ForeignKey(Seminar, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Attendees Name', max_length=255)
    age = models.PositiveIntegerField()
    mobile_no=PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    email = models.EmailField(blank=True, null=True)
    def __str__(self):
        return f'{self.name}-{self.age}-{self.mobile_no}-{self.email}'

