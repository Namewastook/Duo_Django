import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile 


# Create your views here.

@login_required(login_url='/')
def index(request):
    return render(request, "Profile/profile.html")




def add_profile(request): 

    if request.method =="POST":

        new_profile = Profile(first=request.POST['first'],
                            last=request.POST['last'],
                            username=request.POST['username'],
                            aboutyou=request.POST['aboutyou'])
        
        new_profile.save()        

        context = {
            to
        }

        return redirect('profile/Profile.html')

    return render(request, 'profile/Profile.html')

# def delete_profile(request, id):
#     to_delete = Person.objects.get(id=id)
#     to_delete.delete()
#     return redirect('directory')

#     context = {
#         "id": id
#     }
    
#     return render(request, 'profile/delete.html', context=context)

def update_profile(request, id):
    to_update = Person.objects.get(id=id)
    if request.method == "POST":

        
        for key, value in request.POST.items():
            
            if (value and key != "csrfmiddlewaretoken"):
                setattr(to_update, key, value)

            to_update.save()

        
        return redirect('directory')

    context = {
        "id": id,
        "update_profile":to_update
    }
    
    return render(request, 'profile/Profile.html', context=context)


# # This is how we get the Label(Name) of the recipe
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
