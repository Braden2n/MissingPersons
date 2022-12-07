from django.urls import path
from .views import indexPageView, informationPageView, searchPageView, addPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path("information/", informationPageView, name="information"),
    path("search/", searchPageView, name="search"),
    path("add/", addPageView, name="add")
]
