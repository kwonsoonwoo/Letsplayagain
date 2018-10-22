from django.shortcuts import render

from .models import Toylibrary


def toylibrary_list(request):
    toylibraries = Toylibrary.objects.all()
    context = {
        'toylibraries': toylibraries,
    }
    return render(request, 'toylibrary/toylibrary_list.html', context)


def toylibrary_detail(request, pk):
    toylibrary = Toylibrary.objects.get(pk=pk)
    context = {
        'toylibrary': toylibrary,
    }
    return render(request, 'toylibrary/toylibrary_detail.html', context)
