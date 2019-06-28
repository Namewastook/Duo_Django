import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dataclasses import dataclass


# Create your views here.

@login_required(login_url='/')
def index(request):
    return render(request, "Profile/profile.html")


@login_required(login_url="/")
def index(request):
    return render(request, "Profile/profile.html")


req = requests.get(
    "https://api.edamam.com/search?q=chicken&app_id=0890373f&app_key=5c5cb11c82dd77cd32e808aa96589367").json()


# Working with dataclass to try to make this work

# @dataclass
# class Detail:
#     q: list
# totalWeight: str
# app_id: str

# it didn't work the way I thought it would, may revisit later

# This is how we get everything all at once!

new = req.get('hits')
count = 0
for i in range(10):
    print(new[count].get('recipe').get('label'))
    print(new[count].get('recipe').get('yield'))
    print(new[count].get('recipe').get((("calories"))))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("FAT").get("label"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("FAT").get("quantity"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("FAT").get("unit"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("CHOCDF").get("label"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("CHOCDF").get("quantity"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("CHOCDF").get("unit"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("PROCNT").get("label"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("PROCNT").get("quantity"))
    print(new[count].get('recipe').get(
        (("totalNutrients"))).get("PROCNT").get("unit"))

    count += 1


# This is how we get the Label(Name) of the recipe
# print(req.get("hits")[0].get('recipe').get('label'))

# # This is how we get the Calories of the recipe
# print(req.get("hits")[0].get('recipe').get((("calories"))))

# # this is how we get the fat content
# print(req.get("hits")[0].get('recipe').get((("totalNutrients"))).get("FAT"))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("FAT").get('label'))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("FAT").get('quantity'))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("FAT").get('unit'))

# # this is how we get the carbs
# print(req.get("hits")[0].get('recipe').get((("totalNutrients"))).get("CHOCDF"))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("CHOCDF").get('label'))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("CHOCDF").get('quantity'))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("CHOCDF").get('unit'))

# # this is how we get the protein
# print(req.get("hits")[0].get('recipe').get((("totalNutrients"))).get("PROCNT"))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("PROCNT").get('label'))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("PROCNT").get('quantity'))
# print(req.get("hits")[0].get('recipe').get(
#     (("totalNutrients"))).get("PROCNT").get('unit'))

# # this is how we get the yield (number of servings)
# print(req.get("hits")[0].get('recipe').get((("yield"))))
