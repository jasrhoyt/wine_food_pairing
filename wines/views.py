from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from.models import Red_Wines, White_Wines
from django.template import loader

from django.http import HttpResponse


def index(request):
    wine_list = True
    context = {'wine_list': wine_list}
    return render(request, 'wines/index.html', context)


def index_red(request):
    red_wine_list = Red_Wines.objects.all()
    context = {'red_wine_list': red_wine_list}
    return render(request, 'wines/index_reds.html', context)

def index_white(request):
    white_wine_list = White_Wines.objects.all()
    context = {'white_wine_list': white_wine_list}
    return render(request, 'wines/index_whites.html', context)

def details_red(request, wine_id):
    wine = Red_Wines.objects.filter(pk=wine_id) # get is not traversible, so we use filter
    context = {'wine': wine}
    return render(request, 'wines/details_reds.html', context)

def details_white(request, wine_id):
    wine = White_Wines.objects.filter(pk=wine_id)
    context = {'wine': wine}
    return render(request, 'wines/details_whites.html', context)