from django.db import models


# Create your models here.

class Mobile(models.Model):

    mobile_name=models.CharField(max_length=120,unique=True)
    brand=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    color=models.CharField(max_length=50)
    specification=models.CharField(max_length=350)
    camera=models.CharField(max_length=50)
    ram=models.CharField(max_length=50)
    storage=models.CharField(max_length=40)
    image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
       return self.mobile_name
