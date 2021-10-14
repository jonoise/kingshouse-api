import os
from django.db import models


def image_path(self, filename):
    return os.path.join('products', filename)


class Category(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def products(self):
        return self.products.all()


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=155)
    description = models.TextField()
    image = models.ImageField(upload_to=image_path)
    slug = models.SlugField()
    price = models.PositiveIntegerField()
    points = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'


class Ingredient(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=155)

    def __str__(self) -> str:
        return self.name
