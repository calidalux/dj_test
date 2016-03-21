 # -*- coding: utf-8 -*-
import json
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

class TiresListView(generic.ListView):
    model = Tires
    template_name = 'tires/list.html'

def get_tires(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        tires = Tires.objects.filter(size__icontains = q )[:20]
        results = []
        for tire in tires:
            tire_json = {}
            tire_json = tire.size + " " + tire.brand + " " + tire.model
            #tire_json['id'] = tire.id
            #tire_json['label'] = tire.size
            #tire_json['value'] = tire.model
            results.append(tire_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
