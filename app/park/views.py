from django.http import HttpResponse


def index(request):
    return HttpResponse('index 페이지')

