from django.contrib import admin
from .models import CarModel, CarMake
# from .models import related models


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 10

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    model = CarModel
    inlines = [CarModelInline]
    extra = 10

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    model = CarMake

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)