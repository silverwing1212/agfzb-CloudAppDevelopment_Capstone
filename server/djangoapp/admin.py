from django.contrib import admin
from .models import CarModel, CarMake
# from .models import related models

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    # extra = 10

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    #typeChoices = ['Sedan', 'SUV', 'Wagon', 'Crossover', 'Minivan']
    model = CarModel
    fields = ('type', )
    list_display = ('type', )
    # extra = 10

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    model = CarMake
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)