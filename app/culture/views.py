from django.http import HttpResponse
from django.shortcuts import render


def culture_list(request):
    return render(request, 'culture/culture_list.html')


def culture_detail(request, pk):
    return render(request, 'culture/culture_detail.html')
