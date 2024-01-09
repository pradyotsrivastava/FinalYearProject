from django.contrib import admin

# Register your models here.
from apps.member.models import User, Role

admin.site.register(User)
admin.site.register(Role)