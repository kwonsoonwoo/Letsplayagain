from django.http import HttpResponse


def culture_list(request):
    return HttpResponse('문화행사 인덱스 페이지')
