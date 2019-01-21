from django.db import models
# Create your models here.

class Product(models.Model):
    # id= models.UUIDField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    inventory_count = models.IntegerField(default =0)

class Cart(models.Model):
    # id = models.UUIDField(primary_key=True)
    cart_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0) #check to see if we need to make this a FK

class MetaCart(models.Model):
    # id = models.UUIDField(primary_key=True)
    cart_id = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)