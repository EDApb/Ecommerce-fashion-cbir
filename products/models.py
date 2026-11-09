from django.db import models

class Product(models.Model):
    SIZE_CHOICES = [
        ('XS','XS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
    ]
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    size = models.CharField(max_length=2,choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='products/')
