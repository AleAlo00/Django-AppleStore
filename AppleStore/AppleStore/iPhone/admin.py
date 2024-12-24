from django.contrib import admin
from .models import iPhone

class iPhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'space', 'display')
admin.site.register(iPhone, iPhoneAdmin)