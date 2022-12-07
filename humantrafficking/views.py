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
    return render(request, 'humantrafficking/search.html')


def addPageView(request):
    return render(request, 'humantrafficking/add.html')
