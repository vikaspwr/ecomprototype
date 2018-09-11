__author__ = 'vikas.pwr86@gmail.com'

from app_ecommerce.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'category', 'name',)


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'id', 'name', 'email', 'phone', 'first_name', 'last_name', 'address', 'city', 'state', 'pincode', 'logo',
            'is_active')


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = ProductImages.objects.all()
        image_data = ProductImagesSerializer(image, many=True)
        return image_data.data