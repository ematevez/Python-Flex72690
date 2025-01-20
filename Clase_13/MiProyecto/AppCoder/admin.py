from django.contrib import admin
from .models import Estudiante, Profesor, Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']
    
admin.site.register(Estudiante)
admin.site.register(Profesor)