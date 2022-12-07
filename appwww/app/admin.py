from django.contrib import admin
from . models import Product
# Register your models here.


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'nazwa', 'cena', 'desc', 'kategoria', 'prod_image']
