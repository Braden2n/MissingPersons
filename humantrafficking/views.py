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
