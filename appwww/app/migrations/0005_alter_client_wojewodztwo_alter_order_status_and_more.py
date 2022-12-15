# Generated by Django 4.1.2 on 2022-12-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_client_wojewodztwo_alter_product_kategoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='wojewodztwo',
            field=models.CharField(choices=[('lubelskie', 'lubelskie'), ('zachodniopomorskie', 'zachodniopomorskie'), ('świętokrzyskie', 'świętokrzyskie'), ('podlaskie', 'podlaskie'), ('łódzkie', 'łódzkie'), ('kujawsko-pomorskie', 'kujawsko-pomorskie'), ('pomorskie', 'pomorskie'), ('lubuskie', 'lubuskie'), ('warmińsko-mazurskie', 'warmińsko-mazurskie'), ('małopolskie', 'małopolskie'), ('opolskie', 'opolskie'), ('dolnośląskie', 'dolnośląskie'), ('wielkopolskie', 'wielkopolskie'), ('śląskie', 'śląskie')], max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Dostarczone', 'Dostarczone'), ('Zaakceptowane', 'Zaakceptowane'), ('W drodze', 'W drodze'), ('Spakowane', 'Spakowane'), ('Anulowane', 'Anulowane'), ('Woczekiwaniu', 'Woczekiwaniu')], default='Wtrakcie', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='kategoria',
            field=models.CharField(choices=[('BUR', 'Burger'), ('WIN', 'Chicken wings'), ('PIZ', 'Pizza'), ('KEB', 'Kebab'), ('ONI', 'Onion rings'), ('SUS', 'Sushi')], max_length=3),
        ),
    ]