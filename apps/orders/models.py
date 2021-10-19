from django.db import models
from apps.accounts.models import MainUser
from apps.products.models import Product
from django.contrib.postgres.fields import ArrayField


class Order(models.Model):
    code = models.CharField(max_length=255)
    user = models.ForeignKey(
        MainUser, on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    valid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Order {self.code}'


class OrderProduct(models.Model):
    code = models.CharField(max_length=255)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_products')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    ingredients = ArrayField(models.CharField(
        max_length=255, blank=True, null=True))
    extras = ArrayField(models.CharField(
        max_length=255, blank=True, null=True))

    def __str__(self) -> str:
        return f'Producto ordenado: {self.product.name}'


class BillingAddress(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='address')
    full_name = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    city = models.CharField(max_length=155)
    address = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'Dirección orden {self.order.code}'
