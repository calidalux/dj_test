 # -*- coding: utf-8 -*-
import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q

import pdb

from .models import Tires

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Начинаем продавать шины")

class DetailView(generic.DetailView):
    model = Tires
    template_name = 'tires/detail.html'

class TiresListView(generic.ListView):
    model = Tires
    template_name = 'tires/list.html'

def get_tires(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        tires = Tires.objects.filter(fullName__icontains = q )[:20]
        results = []
        for tire in tires:
            tire_json = {}
            tire_json = tire.fullName
            results.append(tire_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

class SearchListView(generic.ListView):
    model = Tires
    template_name = 'tires/list.html'
    def get_queryset(self):
        try:
            #name = self.kwargs['search']
            name = self.request.GET.get('search')
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(fullName__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list
