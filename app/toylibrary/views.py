import json

from django.shortcuts import render

from .models import Toylibrary


def toylibrary_list(request):
    toylibraries = Toylibrary.objects.all()
    context = {
        'toylibraries': toylibraries,
    }
    return render(request, 'toylibrary/toylibrary_list.html', context)
