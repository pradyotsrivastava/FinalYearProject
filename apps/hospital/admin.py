from django.contrib import admin
from .models import *

admin.site.register(Hospital)
admin.site.register(HospitalInfo)
admin.site.register(Treatment)
admin.site.register(HospitalAdmin)
admin.site.register(Doctors)

# Register your models here.
