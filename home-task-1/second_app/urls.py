from django.urls import path
from second_app.views import index, catalog, catalog2

urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('catalog2/', catalog2),
]
