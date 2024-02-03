# Generated by Django 5.0.1 on 2024-02-01 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_address_city_alter_address_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Is Teacher'),
        ),
    ]