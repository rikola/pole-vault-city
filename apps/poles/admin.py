from django.contrib import admin

from .models import Pole, Customer, Rental

# Register your models here.
admin.site.register(Pole)
admin.site.register(Customer)
admin.site.register(Rental)
