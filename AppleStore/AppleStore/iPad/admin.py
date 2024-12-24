from django.contrib import admin
from .models import iPad

# Register your models here.
class iPadAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(iPad, iPadAdmin)