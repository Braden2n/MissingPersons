from django.shortcuts import render, redirect
from .models import Person

# Create your views here.


def indexPageView(request):
    persons = Person.objects.all()

    context = {
        "persons": persons
    }

    return render(request, 'humantrafficking/index.html', context)


def informationPageView(request):
    return render(request, 'humantrafficking/information.html')


def searchPageView(request):

    try:
        name = request.GET('first_name')
        persons = Person.objects.filter(first_name=name)
    except:
        persons = Person.objects.all()

    context = {
        "persons": persons
    }

    return render(request, 'humantrafficking/search.html', context)


def addPageView(request):
    if request.method == "POST":
       date_missing = request.POST["date_at_missing"]
       last_name = request.POST["last_name"]
       first_name = request.POST["first_name"]
       age_at_missing = request.POST["age_at_missing"]
       city = request.POST["city"]
       state = request.POST["state"]
       gender = request.POST["gender"]
       race = request.POST["race"]

       new_person = Person()

       new_person.date_missing = date_missing
       new_person.last_name = last_name
       new_person.first_name = first_name
       new_person.age_at_missing = age_at_missing
       new_person.city = city
       new_person.state = state
       new_person.gender = gender
       new_person.race = race

       new_person.save()

       return redirect("index")
    else:
        persons = Person.objects.all()

    context = {
        "persons": persons
    }
    return render(request, 'humantrafficking/add.html', context)
