from django.contrib import admin
from .models import FixedCharges, Religion, Vehicle, Priest, Cremation

admin.site.register(FixedCharges)
admin.site.register(Religion)
admin.site.register(Vehicle)
admin.site.register(Priest)
admin.site.register(Cremation)
