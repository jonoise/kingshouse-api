from django.db import models
from apps.accounts.models import MainUser
from apps.products.models import Product
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        MainUser, on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    city = models.CharField(max_length=155)
    address = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.get_absolute_url}/{self.slug}'


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_products')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'Producto ordenado: {self.product.name}'
