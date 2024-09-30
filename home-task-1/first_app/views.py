from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('First app')

def catalog(request):
    return HttpResponse('First app * Catalog')

def catalog2(request):
    return HttpResponse('First app * Catalog2')
