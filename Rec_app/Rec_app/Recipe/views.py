import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import FoodCombo


# Create your views here.

# @login_required(login_url='/')
# def index(request):
#     return render(request, "Recipe/recipe.html")


# @login_required(login_url='/')
# def tester(request):
#     response = requests.get(
#         "https://api.edamam.com/search?q=chicken&app_id=0890373f&app_key=5c5cb11c82dd77cd32e808aa96589367").json()

#     meals = []
#     if response:
#         for i in response['hits']:
#             meals.append(i.get('recipe').get('label'))
#     else:
#         print("This didn't work")

#     context = {
#         "response": meals
#     }

#     return render(request, "Recipe/recipe.html", context)

# Chicken Beef and Tofu are the views needed for main dish
# Bean(s) carrots and kale veggies
# pasta eggs and tomato for side dishes


@login_required(login_url='/')
def index(request):
    return render(request, "Recipe/recipe.html")

# def add_profile(request):
#     if request.method =="POST":

def testing(request):
    if request.method == "POST":

        main = request.POST.get("main")
        side = request.POST.get("side")
        extras = request.POST.get("extras")
        dishName = (main + "," + side + "," + extras)

        new_combo = FoodCombo(
            main=main,
            side=side,
            extras=extras,
            dishName=dishName
        )

        print(main)
        print(new_combo)
        print(new_combo.main)
        print(dishName)
        new_combo.save()

        context = {
            "response": new_combo
        }

        return render(request, "Recipe/recipe.html")