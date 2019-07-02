from django.db import models


class FoodCombo(models.Model):
    main = models.CharField(max_length=50)
    side = models.CharField(max_length=50)
    extras = models.CharField(max_length=50)
    dishName = models.CharField(max_length=50)
