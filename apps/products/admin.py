from django.contrib import admin
from .models import Extra, Product, Category, Ingredient
# Register your models here.

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(Extra)
