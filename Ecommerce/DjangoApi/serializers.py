from dataclasses import field, fields
from rest_framework import serializers
from .models import Category,Book,Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'autohor', 
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created'

        ) 
        model = Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imagUrl',
            'status',
            'date_created'

        )
        model = Product