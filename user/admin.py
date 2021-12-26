from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(BicepsCurl)
admin.site.register(Squat)
admin.site.register(PushUp)