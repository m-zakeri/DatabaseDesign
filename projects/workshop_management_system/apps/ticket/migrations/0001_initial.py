# Generated by Django 5.0.1 on 2024-02-04 16:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('status', models.CharField(choices=[('Read', 'read'), ('Unread', 'unread')], default='Unread', max_length=50, verbose_name='Status')),
                ('priority', models.CharField(max_length=50, verbose_name='Priority')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Is Publish')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='course.course', verbose_name='Course')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='ticket.ticket', verbose_name='Parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
