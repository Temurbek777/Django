from django.db import models

# Create your models here.


class TopSellingProducts(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    number_sold = models.FloatField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)


class Cards(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField(max_length=250)


class Profile_Detail(models.Model):
    full_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    job = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    about = models.TextField(max_length=250)
