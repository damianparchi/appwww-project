from django.contrib import admin
from . models import Product, Client, Basket, Payment, Order
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group
# Register your models here.


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'nazwa', 'cena', 'desc', 'kategoria', 'prod_image']

@admin.register(Client)
class ClientModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'miasto', 'numer_domu_mieszkania', 'wojewodztwo', 'telefon', 'kodPocztowy']

@admin.register(Basket)
class BasketModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'amount']
    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk]) #link
        return format_html('<a href="{}">{}</a>', link, obj.product.nazwa) #podaj nazwe przedmiotu do linka i funkcja products do displaylist

@admin.register(Payment)
class PaymentModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'cena', 'orderId','paymentStatus','paymentId', 'oplacone']

@admin.register(Order)
class OrderModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'clients', 'products', 'ilosc', 'dataZamowienia','status', 'platnosci']
    def clients(self, obj):
        link = reverse('admin:app_client_change', args = [obj.client.pk])
        return format_html('<a href="{}">{}</a>', link, obj.client.imie)

    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.nazwa)

    def platnosci(self, obj):
        link = reverse("admin:app_payment_change", args=[obj.platnosc.pk])
        return format_html('<a href="{}">{}</a>', link, obj.platnosc.paymentId)

admin.site.unregister(Group)


