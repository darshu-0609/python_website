from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    #category_choices = []
    name = models.CharField(max_length=40)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2056)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Offer(models.Model):
    discount_code = models.CharField(max_length=10)
    discount_description = models.CharField(max_length=100)
    discount_value = models.FloatField()   


