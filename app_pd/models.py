import uuid
from django.db import models

class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)  # Explicit primary key
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, db_column='CATEGORY', to_field="category_id")

    def __str__(self):
        return self.name
