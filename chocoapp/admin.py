from django.contrib import admin
from .models import Chocolate

class ChocoalateAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']

admin.site.register(Chocolate,ChocoalateAdmin)

