from ast import keyword
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.models import Product, ReviewRating
from .serializers import Product_Serializer
import requests
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters




# Create your views here.
# class ProductReview_APIView(APIView):
    

#     def get(self, request, *args, **kwargs):
       
#         datas = Product.objects.all()
#         serializer = Product_Serializer(datas, many=True)
#         
#         filter_backends = [DjangoFilterBackend]
#         filterset_fields = ['product_name', 'description']

#         return Response(serializer.data, status=status.HTTP_200_OK)

class ProductReview_APIView(generics.ListAPIView):
        model = Product
        queryset = Product.objects.all()
        serializer_class = Product_Serializer
        
        filter_backends = [filters.SearchFilter]

        search_fields = ['product_name']
    

    

def test(request):
    keyword = 'adidas navy'
    responses = requests.get(f'http://127.0.0.1:8000/shoEasy-api/?search={keyword}').json()
    print(responses)
    for response in responses:
        print(response)
        print(response['product_name'])
        print(response['reviews'])
        print(response['category']['category_name'])

    return HttpResponse('Hey Searching is successful man..')
        