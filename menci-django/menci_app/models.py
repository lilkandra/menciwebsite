from django.db import models
from datetime import datetime

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    description = models.CharField(max_length=1000)
    main_image = models.ImageField(upload_to='static/assets')
    scnd_image = models.ImageField(upload_to='static/assets')

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    price = models.PositiveBigIntegerField(default=0)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()

class Bag(models.Model):
    session = models.CharField(max_length=1000000, default='', null=True)
    items = models.ManyToManyField(Item)
    total = models.PositiveIntegerField(default=0)
    validated = models.BooleanField(default=False)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)

class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)