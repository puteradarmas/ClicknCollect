from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name