from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_list_or_404, get_object_or_404
from importlib.util import resolve_name
from rest_framework import status
from products import serializers



@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


