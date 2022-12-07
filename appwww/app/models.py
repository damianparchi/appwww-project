from django.db import models

# Create your models here.

FOOD_CHOICES = {
    ('BUR', 'Burger'),
    ('PIZ', 'Pizza'),
    ('SUS', 'Sushi'),
    ('KEB', 'Kebab'),
    ('WIN', 'Chicken wings'),
    ('ONI', 'Onion rings'),
}

class Product(models.Model):
    nazwa = models.CharField(max_length=255);
    cena = models.FloatField()
    desc = models.TextField()
    kategoria = models.CharField(choices = FOOD_CHOICES, max_length=3)
    prod_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.nazwa
