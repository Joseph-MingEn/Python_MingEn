from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    SPECIES_CHOICES = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, choices=SPECIES_CHOICES, default=DOG)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
