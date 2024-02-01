# Generated by Django 5.0.1 on 2024-01-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponcode',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='user_costumer',
            field=models.ManyToManyField(blank=True, related_name='coupon_code', to='customer.customer', verbose_name='User Costumer'),
        ),
    ]