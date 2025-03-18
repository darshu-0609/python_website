from django.db import models

class  Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2056)

class Offer(models.Model):
    discount_code = models.CharField(max_length=10)
    discount_description = models.CharField(max_length=100)
    discount_value = models.FloatField()   

