from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

""" def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create',

        '/api/products/upload',

        '/api/products/<id>/reivews',

        '/api/products/top',
        '/api/products/<id>/',
        
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/'
    ]
    return JsonResponse(routes, safe=False) """
    