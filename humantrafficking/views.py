from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    return render(request, 'humantrafficking/index.html')


def informationPageView(request):
    return render(request, 'humantrafficking/information.html')
