from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    create_date = models.DateTimeField(default=now, blank=False, null=False)
    create_by = models.ForeignKey(User, blank=True, null=False)
    last_update_date_time = models.DateTimeField(default=now, blank=True, null=True)
    last_update_by = models.ForeignKey(User, blank=True, null=False, related_name='CategoryLastUpdatedBy')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    create_date = models.DateTimeField(default=now, blank=False, null=False)
    create_by = models.ForeignKey(User, blank=True, null=False)
    last_update_date_time = models.DateTimeField(default=now, blank=True, null=True)
    last_update_by = models.ForeignKey(User, blank=True, null=False, related_name='SubCategoryLastUpdatedBy')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200, null=False)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    address = models.TextField(max_length=2000, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(blank=False, null=True)
    phone = models.BigIntegerField(blank=False, null=False)
    email = models.EmailField(max_length=100, null=False)
    create_date = models.DateTimeField(default=now, null=True)
    create_by = models.ForeignKey(User, blank=True, null=True)
    last_update_date_time = models.DateTimeField(default=now, null=True)
    last_update_by = models.ForeignKey(User, blank=True, null=False, related_name='SupplierLastUpdatedBy')
    logo = models.ImageField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    supplier = models.ForeignKey(Supplier)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=False, null=False)
    sku = models.CharField(unique=True, max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=True, null=False)
    quantity = models.IntegerField(blank=True, null=False)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=now, blank=False, null=False)
    create_by = models.ForeignKey(User, blank=True, null=False)
    last_update_date_time = models.DateTimeField(default=now, blank=True, null=True)
    last_update_by = models.ForeignKey(User, blank=True, null=False, related_name='ProductLastUpdatedBy')

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(blank=True, null=True)
    create_date = models.DateTimeField(default=now, blank=False, null=False)
    create_by = models.ForeignKey(User, blank=True, null=False)
    last_update_date_time = models.DateTimeField(default=now, blank=True, null=True)
    last_update_by = models.ForeignKey(User, blank=True, null=False, related_name='ProductImageLastUpdatedBy')

    def __str__(self):
        return self.product.name
