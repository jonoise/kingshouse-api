from rest_framework import serializers
from .models import Category, Product


#########################
## CATEGORY SERIALIZER ##
#########################

class CategorySerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = CategorySerializerProduct(many=True)

    class Meta:
        model = Category
        fields = '__all__'
        extra_fields = ['products']


########################
## PRODUCT SERIALIZER ##
########################

class ProductSerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = ProductSerializerCategory()

    class Meta:
        model = Product
        fields = '__all__'
