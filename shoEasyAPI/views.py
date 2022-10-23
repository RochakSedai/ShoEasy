from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from store.models import Product, ReviewRating
from .serializers import Product_Serializer, ReviewRating_Serializer
import requests

# Create your views here.
class ProductReview_APIView(APIView):

    def get(self, request, *args, **kwargs):
        datas = ReviewRating.objects.all()
        serializer = ReviewRating_Serializer(datas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


def test(request):
    responses = requests.get('http://127.0.0.1:8000/shoEasy-api/').json()
    print(responses)
    for response in responses:
        print(response)
        print(response['product']['product_name'])
        print(response['review'])
        #print(response['product']['product_name'].rating)
        #print(list(response.product_name))