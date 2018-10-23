from django.http import HttpResponse


def index(request):
    return HttpResponse('키즈카페 인덱스')
