from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.IntegerField(help_text="Price in cents (e.g. 1000 = $10.00)") 
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return self.name