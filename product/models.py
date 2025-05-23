from django.db import models
from django.urls import reverse
class Category(models.Model):
    
    name= models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"])
        ]
        verbose_name = "категория"
        verbose_name_plural = "категория"
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category",
        args=[self.slug])
        
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to="products/%d/%m/%Y",
        blank=True
    )
    dascription = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2 ,
    )
    available=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["name"]
        verbose_name = "товар"
        verbose_name_plural = "товары"
        indexes = [
            models.Index(fields=["id","slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_detail",
        args=[self.id,self.slug])
        
