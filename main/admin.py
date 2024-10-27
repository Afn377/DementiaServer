from django.contrib import admin
from .models import Picture
from main.models import Profile

# Register your models here.



admin.site.register(Picture)
# admin.site.register(Profile)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'score1', 'score2', 'score3')
    search_fields = ('user__username',)