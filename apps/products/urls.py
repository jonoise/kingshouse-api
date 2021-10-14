from django.urls import path
from .views import CategoryView, ProductView

urlpatterns = [
    path('', ProductView.as_view(), name='product-view'),
    path('categories/', CategoryView.as_view(), name='product-categories')
]
