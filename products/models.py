from django.db import models

# Create your models here.

class ProductModel(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    discount = models.FloatField()


class ProductImageModel(models.Model):

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')