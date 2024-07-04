from django.db import models

# Create your models here.
# tracker/models.py

from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    # class Food(models.Model):
    #  name = models.CharField(max_length=255)
    # calories = models.IntegerField()

    # def __str__(self):
    #     return self.name
