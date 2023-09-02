from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mob=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    image=models.ImageField(upload_to="image/",null=True)
    def __str__(self):
	    return self.user
    
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    def __str__(self):
	    return self.category_name
        
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to="product/",null=True)
    def __str__(self):
	    return self.product_name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.quantity * self.product.price 