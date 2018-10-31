from django.shortcuts import render

from .models import Culture


def culture_list(request):
    cultures = Culture.objects.all()
    context = {
        'cultures': cultures,
    }
    return render(request, 'culture/culture_list.html', context)


def culture_detail(request, pk):
    culture = Culture.objects.get(pk=pk)
    context = {
        'culture': culture,
    }
    return render(request, 'culture/culture_detail.html', context)
