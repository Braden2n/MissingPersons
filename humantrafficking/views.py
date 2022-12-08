from django.shortcuts import render
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
    return render(request, 'humantrafficking/add.html')
