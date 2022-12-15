from django.db import models
from django.contrib.auth.models import User

# Create your models here.

FOOD_CHOICES = {
    ('BUR', 'Burger'),
    ('PIZ', 'Pizza'),
    ('SUS', 'Sushi'),
    ('KEB', 'Kebab'),
    ('WIN', 'Chicken wings'),
    ('ONI', 'Onion rings'),
}

WOJEWODZTWO_CHOICES = {
    ('dolnośląskie', 'dolnośląskie'),
    ('kujawsko-pomorskie', 'kujawsko-pomorskie'),
    ('lubelskie', 'lubelskie'),
    ('lubuskie', 'lubuskie'),
    ('łódzkie', 'łódzkie'),
    ('małopolskie', 'małopolskie'),
    ('opolskie', 'opolskie'),
    ('podlaskie', 'podlaskie'),
    ('pomorskie', 'pomorskie'),
    ('śląskie', 'śląskie'),
    ('świętokrzyskie', 'świętokrzyskie'),
    ('warmińsko-mazurskie', 'warmińsko-mazurskie'),
    ('wielkopolskie', 'wielkopolskie'),
    ('zachodniopomorskie', 'zachodniopomorskie'),
}

STATUS_CHOICES = {
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
}

class Product(models.Model):
    nazwa = models.CharField(max_length=255)
    cena = models.FloatField()
    desc = models.TextField()
    kategoria = models.CharField(choices = FOOD_CHOICES, max_length=3)
    prod_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.nazwa


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length = 255)
    miasto = models.CharField(max_length = 255)
    ulica = models.CharField(max_length = 255)
    numer_domu_mieszkania = models.IntegerField(max_length = 3)
    telefon = models.IntegerField(default = 0)
    kodPocztowy = models.IntegerField()
    wojewodztwo = models.CharField(choices = WOJEWODZTWO_CHOICES, max_length=50)
    def __str__(self):
        return self.imie

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    @property
    def totalCost(self):
        return self.amount * self.product.cena

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cena = models.FloatField()
    orderId = models.CharField(max_length=100, blank=True, null=True)
    paymentStatus = models.CharField(max_length=100, blank=True, null=True)
    paymentId = models.CharField(max_length=100, blank=True, null=True)
    oplacone = models.BooleanField(default=False)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dataZamowienia = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices = STATUS_CHOICES, default="Pending")
    ilosc = models.PositiveBigIntegerField(default=1)
    platnosc = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    @property
    def totalCost(self):
        return self.ilosc * self.product.cena

