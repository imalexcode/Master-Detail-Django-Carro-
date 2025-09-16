from django.contrib import admin
from .models import Carro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'cor', 'valor')
    search_fields = ('modelo', 'cor')
