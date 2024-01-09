from django.contrib import admin

# Register your models here.
from .models import City,State,Specialization

admin.site.register(Specialization)
admin.site.register(State)
admin.site.register(City)
