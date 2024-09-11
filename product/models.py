from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=100, null=True,blank=True)
    capacity = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    generation = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    cpu_model = models.CharField(max_length=100, null=True, blank=True)
    hard_disk_size = models.CharField(max_length=50, null=True, blank=True)
    strap_color = models.CharField(max_length=100, null=True, blank=True)
    case_size = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
