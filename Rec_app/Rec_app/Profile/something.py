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

new = req.get('hits')

z = ["label", "yield", "calories"]
a = ["label", "quantity", "unit"]
n = ["FAT", "CHOCDF", "PROCNT"]

for x, y in enumerate(new):
    for i in z:
        print(new[x]['recipe'][i])
    for l in n:
        for c in a:
            print(new[x]['recipe']["totalNutrients"][l][c])
