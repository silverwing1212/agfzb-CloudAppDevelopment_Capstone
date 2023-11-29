from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = model.CharField(null=False, max_length=100)

    def __str__(self):
        return "{" + self.name + ", " + self.description + "}"


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    typeChoices = ['Sedan', 'SUV', 'Wagon', 'Crossover', 'Minivan']
    name = models.CharField(null=False, max_length=30)
    carMake = model.ManyToOne(CarMake)
    type = model.CharField(null=False, max_length=30, choices=typeChoices, default='Sedan')
    year = model.DateField()

    def __str__(self):
        return "{" + self.name + ", " + str(self.type) + ", " + str(self.year) + "}"


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    pass


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    pass
