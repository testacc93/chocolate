from django.contrib import admin
from .models import Chocolate, Query

class ChocoalateAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']

admin.site.register(Chocolate,ChocoalateAdmin)

class QueryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

admin.site.register(Query,QueryAdmin)
