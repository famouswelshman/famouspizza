from django.db import models

# Create your models here.

class Deals(models.Model):
    category = models.ForeignKey('deals', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=175)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Deals'

    def __str__(self):
        return self.name
