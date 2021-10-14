from rest_framework import views, permissions, status
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        category = Category.objects.all()
        s = CategorySerializer(category, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)


class ProductView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        p = Product.objects.all()
        s = ProductSerializer(p, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)
