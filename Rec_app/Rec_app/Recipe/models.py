from django.db import models


# Create your models here.

# model is for dietary checkboxes from profile


class FoodCombo(models.Model):
    main = models.CharField(max_length=50)
    side = models.CharField(max_length=50)
    extras = models.CharField(max_length=50)
    dishName = models.CharField(max_length=50)


