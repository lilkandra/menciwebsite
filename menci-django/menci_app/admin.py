from django.contrib import admin
from .models import Product, Client, Item, Bag, Order, Message

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Bag)
admin.site.register(Order)
admin.site.register(Message)