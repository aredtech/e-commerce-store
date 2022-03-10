from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.1)])
    description = models.TextField()
    stock = models.IntegerField(validators=[MinValueValidator(1)])
    slug = models.SlugField()
    last_update = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey("Collection", on_delete=models.PROTECT)
    product = models.ManyToManyField("Promotion", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

class Promotion(models.Model):
    title = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]



