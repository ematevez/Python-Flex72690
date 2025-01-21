from django.contrib import admin
from .models import Estudiante, Profesor
from .models import Profile
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']
