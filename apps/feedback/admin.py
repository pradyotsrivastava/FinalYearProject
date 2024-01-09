from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FeedbackCremation)
admin.site.register(FeedbackNgo)
admin.site.register(FeedbackHospital)
admin.site.register(FeedbackSeminar)
admin.site.register(FeedbackDoctor)
