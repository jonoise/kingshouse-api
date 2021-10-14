from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=155)
    slug = models.SlugField()
    price = models.PositiveIntegerField()
    points = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.get_absolute_url}/{self.slug}'


class Ingredient(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=155)

    def __str__(self) -> str:
        return self.name
