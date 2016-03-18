 # -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Tires

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Начинаем продавать шины")

class DetailView(generic.DetailView):
    model = Tires
    template_name = 'tires/detail.html'
