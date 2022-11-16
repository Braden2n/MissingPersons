from django.urls import path
from .views import indexPageView, informationPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path("information/", informationPageView, name="information")
]
