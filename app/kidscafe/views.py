from django.shortcuts import render

from .models import Kidscafe


def kidscafe_list(request):
    kidscafes = Kidscafe.objects.all()
    context = {
        'kidscafes': kidscafes,
    }
    return render(request, 'kidscafe/kidscafe_list.html', context)


def kidscafe_detail(request, pk):
    kidscafe = Kidscafe.objects.get(pk=pk)
    context = {
        'kidscafe': kidscafe,
    }
    return render(request, 'kidscafe/kidscafe_detail.html', context)
