import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import FoodCombo, Seed_Db


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

        new_combo.save()

        response = eval(
            f'requests.get("https://api.edamam.com/search?q={dishName}&app_id=0890373f&app_key=5c5cb11c82dd77cd32e808aa96589367").json()')

        meals = []
        if response:
            for i in response['hits']:
                x = "Recipe name: "
                x += (i.get('recipe').get('label'))
                x += " Servings: "
                x += str(int(i.get('recipe').get('yield')))
                x += " Calories: "
                x += str(int(i.get('recipe').get('calories')))
                for y in response["hits"]:
                    a = " Contains: "
                    a += str(int((y.get('recipe').get("totalNutrients").get("FAT").get("quantity"))))
                    a += "g of Fat "
                    a += str(int((y.get('recipe').get("totalNutrients").get("CHOCDF").get("quantity"))))
                    a += "g of Carbs "
                    a += str(int((y.get('recipe').get("totalNutrients").get("PROCNT").get("quantity"))))
                    a += "g of Protein"

                meals.append(x)
                meals.append(a)

        else:
            print("This didn't work")

        context = {
            "response": meals
        }

        return render(request, "Recipe/recipe.html", context)


def seeding_db(request):
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

        new_combo.save()

    response = eval(
        f'requests.get("https://api.edamam.com/search?q={dishName}&app_id=0890373f&app_key=5c5cb11c82dd77cd32e808aa96589367").json()')

    rec_label = []
    rec_yield = []
    rec_calories = []
    rec_fat_quanity = []
    rec_carbs_quanity = []
    rec_protein_quanity = []

    for i in response['hits']:
        x = (i.get('recipe').get('label'))
        y = str(int(i.get('recipe').get('yield')))
        z = str(int(i.get('recipe').get('calories')))
        for y in response["hits"]:
            uno = str(
                int((y.get('recipe').get("totalNutrients").get("FAT").get("quantity"))))
            dos = str(
                int((y.get('recipe').get("totalNutrients").get("CHOCDF").get("quantity"))))
            tres = str(
                int((y.get('recipe').get("totalNutrients").get("PROCNT").get("quantity"))))

    rec_label.append(x)
    rec_yield.append(y)
    rec_calories.append(z)
    rec_fat_quanity.append(uno)
    rec_carbs_quanity.append(dos)
    rec_protein_quanity.append(tres)

    seeded_db = Seed_Db(
        rec_label=rec_label,
        rec_yield=rec_yield,
        rec_calories=rec_calories,
        rec_fat_quanity=rec_fat_quanity,
        rec_carbs_quanity=rec_carbs_quanity,
        rec_protein_quanity=rec_protein_quanity,
        foodcombo=new_combo
    )

    seeded_db.save()

    return HttpResponse("It worked?")


# def another_view(request):

#     Seed_Db()

#     return render(request, "Recipe/recipe.html", context)
