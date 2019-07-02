from django.db import models


# Create your models here.

# model is for dietary checkboxes from profile

# class Profile(models.Model):
#     DIET_CHOICES = (
#         ('Dairy Free', "Egg Free", "Fish Free"),
#         ('Gluten Free', 'Keto Friendly', "Kosher"),
#         ("Peanuts", "Vegan", "Vegetarian")
#     )
#     selection = models.BooleanField(max_length = 30, selection = DIET_CHOICES)

class FoodCombo(models.Model):
    main = models.CharField(max_length=50)
    side = models.CharField(max_length=50)
    extras = models.CharField(max_length=50)
    dishName = models.CharField(max_length=50)