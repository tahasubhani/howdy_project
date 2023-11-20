from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural = 'categories'

    
    def __str__(self):
        return f'Name: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='howdy/products/')
    price = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6, blank=True, null=True)

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    sub_total =models.DecimalField( default=0,decimal_places=2, max_digits=8)
    order_id =models.CharField(default=0, max_length=15)



    def __str__(self):
        # return f'Name: {self.product.name}'
        return f" {self.user.username} - {self.sub_total}"
    

class Order(models.Model):
    first_name =models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    city =models.CharField(max_length=100)
    phone =models.CharField(max_length=15)
    address =models.CharField(max_length=500)
    Special_Instructions =models.CharField(max_length=500 ,null=True,blank=True)
    payment_mode =models.CharField(max_length=50)
    user =models.ForeignKey("User",on_delete=models.CASCADE)
    oders_amount=models.DecimalField(default=0,decimal_places=2,max_digits=8)

    def __str__(self):
        return f" {self.user.username} - {self.oders_amount} "
    

class User(AbstractUser):
    phone =models.CharField(max_length=15)
