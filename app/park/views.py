from django.shortcuts import render

from crawling import park_crawling
from .models import Park


def park_list(request):
    park_crawling()
    parks = Park.objects.all()
    context = {
        'parks': parks,
    }
    return render(request, 'park/park_list.html', context)


def park_detail(request, pk):
    park = Park.objects.get(pk=pk)
    context = {
        'park': park,
    }
    return render(request, 'park/park_detail.html', context)
