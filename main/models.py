from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):

    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    tg_id = models.BigIntegerField(null=True, blank=True, unique=True)
    tg_username = models.CharField(max_length=70, null=True, blank=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Product(models.Model):
    title = models.CharField(max_length=225)
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True, blank=True)
    text = models.TextField()
    rasm = models.ImageField(upload_to='photo', null=True, blank=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='blog', null=True, blank=True)
      
    def __str__(self):
        return self.title


class Shop(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)


class Foydali(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    icon = models.ImageField(upload_to='icon', null=True, blank=True)

    def __str__(self):
        return self.title

class Clients(models.Model):
    fi = models.CharField(max_length=234)
    kasb = models.CharField(max_length=234)
    text = models.TextField()
    rasm = models.ImageField(upload_to='client', null=True, blank=True)

    def __str__(self):
        return self.fi