from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Second app')

def catalog(request):
    return HttpResponse('Second app * Catalog')

def catalog2(request):
    return HttpResponse('Second app * Catalog2')
