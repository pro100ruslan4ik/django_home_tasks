from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Third app')

def catalog(request):
    return HttpResponse('Third app * Catalog')

def catalog2(request):
    return HttpResponse('Third app * Catalog2')
