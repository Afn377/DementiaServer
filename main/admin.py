from django.contrib import admin
from .models import Picture
from main.models import Profile

# Register your models here.



admin.site.register(Picture)
admin.site.register(Profile)