# Generated by Django 4.2 on 2024-01-20 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addresses',
            new_name='Address',
        ),
        migrations.RenameIndex(
            model_name='address',
            new_name='users_addre_country_b60bfc_idx',
            old_name='users_addre_country_908629_idx',
        ),
    ]