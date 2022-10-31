from asyncore import read
from dataclasses import fields
from rest_framework import serializers
from store.models import Product, ReviewRating
from category.models import Category

class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class Product_Serializer(serializers.ModelSerializer):
    category = Category_Serializer()
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'images', 'category', 'reviews']

# class ReviewRating_Serializer(serializers.ModelSerializer):
#     product = Product_Serializer()
    
#     class Meta:
#         model = ReviewRating
#         fields = ['product', 'review', 'rating']

   
