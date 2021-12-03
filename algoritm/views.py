from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'algoritm/home.html')


def dual_method(request):
    return render(request, 'algoritm/dual_method_view.html')


def graphical_method(request):
    return render(request, 'algoritm/graphical_method.html')


def north_west_method(request):
    return render(request, 'algoritm/north_west_method.html')
