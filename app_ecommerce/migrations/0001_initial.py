# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-11 09:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('create_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='CategoryLastUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('price', models.IntegerField(blank=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ecommerce.Category')),
                ('create_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProductLastUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('create_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProductImageLastUpdatedBy', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ecommerce.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update_date_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ecommerce.Category')),
                ('create_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='SubCategoryLastUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('address', models.TextField(max_length=2000, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('last_update_date_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('is_active', models.BooleanField(default=False)),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('last_update_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='SupplierLastUpdatedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ecommerce.SubCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ecommerce.Supplier'),
        ),
    ]
