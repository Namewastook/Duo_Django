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

    if request.method == "POST":

        new_profile = Profile(first=request.POST['first'],
                            last=request.POST['last'],
                            username=request.POST['username'],
                            aboutyou=request.POST['aboutyou'])

        new_profile.save()

        return redirect('profile/Profile.html')

    return render(request, 'profile/Profile.html')


def update_profile(request, id):
    to_update = Person.objects.get(id=id)
    if request.method == "POST":

        for key, value in request.POST.items():

            if (value and key != "csrfmiddlewaretoken":
                setattr(to_update, key, value)

        to_update.save()

        return redirect('directory')

    context={
        "id": id,
        "update_profile": to_update
    }

    return render(request, 'profile/Profile.html', context=context)
