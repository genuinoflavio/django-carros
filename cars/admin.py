from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin): 
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'model_year','brand', 'price')
    search_fields = ('model',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)