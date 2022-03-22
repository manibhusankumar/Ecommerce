from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class HomeBanner(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    video_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name = 'Home Banner'
        verbose_name_plural = 'Home Banners'

    def __str__(self):
        return self.title


class LiveSaleSection(models.Model):
    title = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'LiveSaleSection'
        verbose_name_plural = 'LiveSaleSections'

    def __str__(self):
        return self.title

class ShoppingX(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    discount = models.DecimalField(max_digits=19, decimal_places=2, null=True,blank=True)
    slug = models.SlugField(max_length=100, unique=True,null=True, blank=True)



    class Meta:
        verbose_name = 'ShoppingX'
        verbose_name_plural = 'ShoppingXs'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class TrendingDeals(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    discount = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True,null=True, blank=True)


    class Meta:
        verbose_name = 'TrendingDeals'
        verbose_name_plural = 'TrendingDeals'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(ShoppingX,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


class Post(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ('-created',)