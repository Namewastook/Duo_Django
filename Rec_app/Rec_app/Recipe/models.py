from django.db import models


class FoodCombo(models.Model):
    main = models.CharField(max_length=50)
    side = models.CharField(max_length=50)
    extras = models.CharField(max_length=50)
    dishName = models.CharField(max_length=50)


class Seed_Db(models.Model):
    rec_label = models.CharField(max_length=50)
    rec_yield = models.CharField(max_length=50)
    rec_calories = models.CharField(max_length=50)
    rec_fat_quanity = models.CharField(max_length=50)
    rec_carbs_quanity = models.CharField(max_length=50)
    rec_protein_quanity = models.CharField(max_length=50)
    foodcombo = models.ForeignKey(FoodCombo, on_delete=models.CASCADE)
