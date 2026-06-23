from django.contrib import admin
from .models import Court, Booking

# Registrar los modelos para que aparezcan de forma visual
admin.site.register(Court)
admin.site.register(Booking)
# Register your models here.
